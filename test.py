import os
import io
import base64
import hashlib
import random
import string
import tempfile
import time
import uuid
from io import BytesIO

import re
import requests
from PIL import Image
import numpy as np
import pandas as pd
import pickle

import easyocr
#from easyocr import Reader
#from paddleocr import PaddleOCR
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
import streamlit as st
import streamlit_nested_layout
import streamlit.components.v1 as components
import streamlit_scrollable_textbox as stx
import streamlit_extras

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

import webbrowser
from utils import recommendations, read_object


def generate_unique_key():
    unique_id = str(uuid.uuid4())
    hashed_key = hashlib.sha256(unique_id.encode()).hexdigest()
    return hashed_key

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def get_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--no-sandbox')
    options.add_argument('--lang=en-US')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument("--ignore-certificate-errors")
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

def perform_img_actions(url):
    if 'image_links' not in st.session_state:
        st.session_state.image_links = []
    if 'current_image_index' not in st.session_state:
        st.session_state.current_image_index = 0
    try:
        driver.get(url)
    except:
        st.stop()
        pass
    with st.spinner('Loading text & audio..'):
        st.session_state.image_links = get_image_links(url)
        st.session_state.current_image_index = 0
        if st.session_state.image_links:
            for image_link in st.session_state.image_links:
                st.image(image_link, use_column_width=True)
            st.write(f"Total Images: {len(st.session_state.image_links)}")
            transcribe_to_audio(st.session_state.image_links)

def get_image_links(url):
    driver = get_driver()
    try:
        driver.get(url)
    except WebDriverException as ex:
        if driver.current_url == url:
            pass
            return []
        else:
            st.stop()
            return []
    image_links = []
    
    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
    for img_element in img_elements:
        img_src = img_element.get_attribute('src')
        if img_src and is_image_link(img_src):
            image_links.append(img_src)
    
    img_elements_with_id = driver.find_elements(By.CSS_SELECTOR, 'img[id^="image-"]')
    for img_element_with_id in img_elements_with_id:
        img_src_with_id = img_element_with_id.get_attribute('src')
        if img_src_with_id and is_image_link(img_src_with_id):
            image_links.append(img_src_with_id)
    
    img_elements_with_class = driver.find_elements(By.CSS_SELECTOR, 'img.wp-manga-chapter-img')
    for img_element_with_class in img_elements_with_class:
        img_src_with_class = img_element_with_class.get_attribute('src')
        if img_src_with_class and is_image_link(img_src_with_class):
            image_links.append(img_src_with_class)
	
    driver.quit()
    return image_links

def transcribe_to_audio(image_links):
    audio_files = []
	
    #ocr = PaddleOCR(use_angle_cls=False, lang='en')
    reader = easyocr.Reader(['ch_tra', 'en'])

    all_text = []  # List to accumulate all text from images
    for idx, img_link in enumerate(image_links, start=1):
        if not is_supported_image_format(img_link):
            continue
        
        with st.spinner(" Getting image text "):
            try:
                img_data = requests.get(img_link).content
                img_file = io.BytesIO(img_data)
                img_webp = Image.open(img_file)
                img_jpg = img_webp.convert('RGB')
                img_jpg.save("converted_img.jpg", 'JPEG')
            except Exception as e:
                continue

            try:
                #listresult = ocr.ocr("converted_img.jpg", det=False, cls=False)
                listresult = reader.readtext(img_jpg, detail = 0, paragraph=True)
                st.write(listresult)
                print(listresult)
                text_string = listresult
                
                text = filter_english_words(str(text_string))
                all_text.append(text)  # Accumulate text from each image
                joined_text = " ".join(all_text)
                st.write("All Text:", joined_text)
                if joined_text:
                    audio_file_path = os.path.join('audio', os.path.splitext(os.path.basename(img_link))[0] + '.mp3')
                    if not os.path.exists(audio_file_path):
                        tts = gTTS(text=text, lang='en', slow=False)
                        tts.save(audio_file_path)
                    audio_files.append(audio_file_path)
                    if on:
                        res_box.markdown(f':blue[Streaming: ]:green[*{text}*]')
                else:
                    res_box.markdown(f':blue[Dao: ]:orange[No Text]')
            except Exception as e:
                st.write(f"Error processing text: {e}")
                text = ""

    return audio_files

def is_supported_image_format(image_url):
    supported_formats = ['.png', '.jpg', '.jpeg', '.webp']
    for format in supported_formats:
        if image_url.lower().endswith(format):
            return True
    return False

def is_image_link(link):
    image_extensions = ['.png', '.jpg', '.jpeg', '.webp']
    for ext in image_extensions:
        if link.lower().endswith(ext):
            return True
    return False


def filter_english_words(text):
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        english_word_pattern = r'\b[a-zA-Z]+(?:\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\'":;\[\]()*&^%$#@`~\\/]|\.\.\.)?\b'
        english_words = re.findall(english_word_pattern, text)
        english_text = ' '.join(english_words)
        text = english_text.lower()
    except Exception as e:
        st.write(f"Error filtering English words: {e}")
        text = ""  # Return empty string if an error occurs
    return text

def obfuscate(text):
	mapping = {}
	for i in range(26):
		mapping[chr(65 + i)] = chr(((i + 1) % 26) + 65)
		mapping[chr(97 + i)] = chr(((i + 1) % 26) + 97) 
	obfuscated_text = ''.join(mapping.get(char, char) for char in text)
	if 'nightcomic.com' in text:
		obfuscated_text = "TOP/" + obfuscated_text
	if 'daotranslate' in text:
		obfuscated_text = "NOVEL/" + obfuscated_text
	if 'manhuaaz.com' in text:
		obfuscated_text = "PANEL/" + obfuscated_text
	return obfuscated_text, mapping

def deobfuscate(obfuscated_text, mapping):
	if obfuscated_text.startswith("TOP/"):
		obfuscated_text = obfuscated_text[len("TOP/"):]
	if obfuscated_text.startswith("NOVEL/"):
		obfuscated_text = obfuscated_text[len("NOVEL/"):]
	if obfuscated_text.startswith("PANEL/"):
		obfuscated_text = obfuscated_text[len("PANEL/"):]
	inverted_mapping = {v: k for k, v in mapping.items()}
	original_text = ''.join(inverted_mapping.get(char, char) for char in obfuscated_text)
	return original_text

history = []
ih = ""
icob = Image.open('static/-.ico')
ranum = random.randint(1,99999)

st.sidebar.write('BlackDao: Manga Dōjutsu')

if 'image_links' not in st.session_state:
    st.session_state.image_links = []
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

genre = None

with st.sidebar:
    on = st.checkbox('Stream Story (Experimental)', value=False, disabled=False)

def resize_image(img_url, scale_factor):
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_image

def resize_displayed_image(img_url, scale_factor):
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    img_byte_array = io.BytesIO()
    resized_image.save(img_byte_array, format="PNG")  # Convert to PNG format for display
    img_byte_array = img_byte_array.getvalue()
    return img_byte_array
		
col1, col2, col3 = st.columns(3)
outer_cols = st.columns([1, 2])
counter = 0
with col1:
    with st.expander(':loud_sound: Novels '):
        st.write('Test')
						
counter2 = 0
with col2:
    with st.expander(f":chart_with_upwards_trend: Top Rated"):
        resp = requests.get("https://mangatx.to/")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_items = soup.find_all("div", {"class": "page-item-detail manga"})
        
            for item in manga_items:
                if counter2 >= 10:  # Check if the counter exceeds 3
                    break
                
                manga_title = item.find("h3", {"class": "h5"}).text.strip()
                manga_link = item.find("a", href=True)['href']
                
                chapter_links = item.select(".list-chapter .chapter-item a.btn-link")
                if chapter_links:
                    chapter_link = chapter_links[0]['href']
                else:
                    chapter_link = ''
                
                st.write(f"[{manga_title}]({chapter_link})")
                
                img_tag = item.find("img", src=True)
                if img_tag:
                    img_url = img_tag['src']
                    try:
                        resized_img_byte_array = resize_displayed_image(img_url, scale_factor=4)
                        st.image(resized_img_byte_array, use_column_width='always')
                    except Exception as e:
                        pass
                obfuscated_text, mapping = obfuscate(chapter_link)
                txt = f"{obfuscated_text}"
                st.code(txt, language='java')
                st.caption('Copy Code')
                st.divider()
                counter2 += 1

counter3 = 0
with col3:
    with st.expander(f":frame_with_picture: Recently Updated"):
        resp = requests.get("https://www.mangaread.org/")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_items = soup.find_all("div", {"class": "page-item-detail manga"})
        
            for item in manga_items:
                if counter3 >= 10:  # Check if the counter exceeds 3
                    break
                
                manga_title = item.find("h3", {"class": "h5"}).text.strip()
                manga_link = item.find("a", href=True)['href']
                
                chapter_links = item.select(".list-chapter .chapter-item a.btn-link")
                if chapter_links:
                    chapter_link = chapter_links[0]['href']
                else:
                    chapter_link = ''
                
                st.write(f"[{manga_title}]({chapter_link})")
                
                img_tag = item.find("img", src=True)
                if img_tag:
                    img_url = img_tag['src']
                    try:
                        resized_img_byte_array = resize_displayed_image(img_url, scale_factor=4)
                        st.image(resized_img_byte_array, use_column_width='always')
                    except Exception as e:
                        pass
                
                chapter_items = item.select(".list-chapter .chapter-item")
                for chapter_item in chapter_items:
                    chapter_name = chapter_item.find("a", class_="btn-link").text.strip()
                    chapter_date = chapter_item.find("span", class_="post-on").text.strip()
                st.write(f"Chapter: {chapter_name}")
                st.write(f"Released: {chapter_date}")
                
                obfuscated_text, mapping = obfuscate(chapter_link)
                txt = f"{obfuscated_text}"
                st.code(txt, language='java')
                st.caption('Copy Code')
                st.divider()
                counter3 += 1

res_box = st.empty()

url = deobfuscate(st.text_input(":orange[Code:]", value='', placeholder="iuuqt://ebhdrrghmbuf.vt/..", key='readfield', help="Enter Manga Code here"), mapping)
col1, col2, col3 = st.columns(3)
with col1:
    ok = st.button(":green_book: Read", help="Read", key='readbutton', use_container_width=False)

if ok:
    if "daotrans" not in url.lower():
        with st.spinner('Loading text & audio..'):
            driver = get_driver()
            st.session_state.image_links = get_image_links(url)
            st.session_state.current_image_index = 0
            if st.session_state.image_links:
                for image_link in st.session_state.image_links:
                    st.image(image_link, use_column_width=True)
                st.write(f"Total Images: {len(st.session_state.image_links)}")
                transcribe_to_audio(st.session_state.image_links)
                oldurl = url
                chap = ''.join([n for n in oldurl if n.isdigit()])
                nxtchap = str(int(chap) + int(+1))
                prvchap = str(int(chap))
                nxtUrl = str(oldurl.replace(chap, nxtchap))
                obfuscated_text, mapping = obfuscate(nxtUrl)
                st.caption(":green[Chapter Complete:] " + prvchap + "\n\n:orange[Next Chapter:] " + obfuscated_text)
                txt = f"""
                {obfuscated_text}
                """
                st.code(txt, language='java')
                st.caption('Copy Code')
 
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
 
