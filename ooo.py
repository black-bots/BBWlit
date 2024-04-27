# ┌──────────────────────────────────┐
# │ BlackDao: Manga Dōjutsu v2.12.21 │
# ├──────────────────────────────────┤
# │ Copyright © 2024 BlackBots.net   │
# │ (https://BlackBots.net)          │
# ├──────────────────────────────────┤
# │ Developer: @Supreme.Ciento       │
# ├──────────────────────────────────┤
# │ Licensed under the MIT           │
# │ (https://BlackBots.net/license)  │
# └──────────────────────────────────┘
#            マンガアプリ
 
# 010011010110000101101110011001110110000101000100011011110110101001110101011101000111001101110101
 
# 77971101039768111106117116115117 
                                                                      
#    x*8888x.:*8888: -"888:                                                                     
#   X   48888X `8888H  8888                                                         
#  X8x.  8888X  8888X  !888>               x@88k u@88c.                  
#  X8888 X8888  88888   "*8%-    us888u.  ^"8888""8888"  .ue888Nc..    us888u.                  
#  '*888!X8888> X8888  xH8>   .@88 "8888"   8888  888R  d88E`"888E` .@88 "8888"                 
#    `?8 `8888  X888X X888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#    -^  '888"  X888  8888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#     dx '88~x. !88~  8888>   9888  9888    8888  888R  888E  888E  9888  9888                  
#   .8888Xf.888x:!    X888X.: 9888  9888   "*88*" 8888" 888& .888E  9888  9888                  
#  :""888":~"888"     `888*"  "888*""888"    ""   'Y"   *888" 888&  "888*""888"                 
#      "~'    "~        ""     ^Y"   ^Y'                 `"   "888E  ^Y"   ^Y'                  
#                                                       .dWi   `88E                             
#                                                       4888~  J8%                              
#                                                        ^"===*"`                               
#         ....                                                          .x+=:.                  
#     .xH888888Hx.                     .                               z`    ^%                 
#   .H8888888888888:     *^^^^^^^*    888>                    .88             <k
#   888*"""?""*88888X    ...ue888b    "8P    .@88k  z88u     :888ooo    .@8Ned8"  .@88k  z88u   
#  'f     d8x.   ^%88k   888R Y888r    .    ~"8888  8888   -*8888888  .@^%8888"  ~"8888  8888   
#  '>    <88888X   '?8   888R I888>  u888u.   8888  888R     8888    x88:  `)8b.   8888  888R   
#   `:..:`888888>    8>  888R I888> `'888E    8888  888R     8888    8888N=*8888   8888  888R   
#          `"*88     X   888R I888>   888E    8888  888R     8888     %8"    R88   8888  888R   
#     .xHHhx.."      !  u8888cJ888    888E    8888 ,888B .  .8888Lu=   @8Wou 9%    8888 ,888B . 
#    X88888888hx. ..!    "*888*P"     888E   "8888Y 8888"   ^%888*   .888888P`    "8888Y 8888"  
#   !   "*888888888"       'Y"        888E    `Y"   'YP       'Y"    `   ^"F       `Y"   'YP    
#          ^"***"`                    888E                                                      
#                                     888E                                                      
#                                     888P                                                      
#                                   .J88" "                                                     
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

import easyocr as ocr  # OCR
from easyocr import Reader
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
import streamlit as st
import streamlit_nested_layout
import streamlit.components.v1 as components
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
    try:
        driver.get(url)
    except WebDriverException as ex:
        if driver.current_url == url:
            pass
            return []
        else:
            st.write(f'Error loading URL: {ex}')
            return []
    image_links = []
    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
    for img_element in img_elements:
        img_src = img_element.get_attribute('src')
        if img_src and is_image_link(img_src):
            image_links.append(img_src)
    driver.quit()
    return image_links

def get_image_links2(url):
    try:
        driver.get(url)
    except WebDriverException as ex:
        if driver.current_url == url:
            pass
            return []
        else:
            st.write(f'Error loading URL: {ex}')
            return []
    image_links = []
    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img[id^="image-"]')
    for img_element in img_elements:
        img_src = img_element.get_attribute('src')
        if img_src and is_image_link(img_src):
            image_links.append(img_src)
    driver.quit()
    return image_links

def transcribe_to_audio(image_links):
    audio_files = []
    reader = load_model()  # Load OCR model outside the loop
    for idx, img_link in enumerate(image_links, start=1):
        if not is_supported_image_format(img_link):
            continue
        
        with st.spinner(" Getting image text "):
            # Download the image
            img_data = requests.get(img_link).content
            
            # Read text from the image
            result = reader.readtext(img_data)
            result_text = [text[1].strip() for text in result]
            
        text = filter_english_words(result_text)
        if text:
            audio_file_path = os.path.join('audio', os.path.splitext(os.path.basename(img_link))[0] + '.mp3')
            if not os.path.exists(audio_file_path):
                tts = gTTS(text=text, lang='en', slow=False)
                tts.save(audio_file_path)
            audio_files.append(audio_file_path)
            if on:
                res_box.markdown(f':blue[RAWR: ]:green[*{text}*]')
        else:
            res_box.markdown(f':blue[Dao: ]:orange[No Text]')
    return audio_files


def is_supported_image_format(image_url):
    supported_formats = ['.png', '.jpg', '.jpeg']
    for format in supported_formats:
        if image_url.lower().endswith(format):
            return True
    return False

def is_image_link(link):
    image_extensions = ['.png', '.jpg', '.jpeg']
    for ext in image_extensions:
        if link.lower().endswith(ext):
            return True
    return False

def load_model() -> Reader:
    return ocr.Reader(["en"], model_storage_directory=".")

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

def readit(url):
    driver = get_driver()
    try:
        driver.get(url)
    except:
        pass
    if not url:
        res_box.markdown(f':blue[Dao: ]:green[*Enter a valid URL before running.*]')
    else:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                d = soup.find("div", {"class": "epcontent entry-content"})
                if d:
                    all_text = ""
                    num_paragraphs = len(d.findAll("p"))
                    paragraphs = d.findAll("p")
                    desired_group_size = 1  # Set your desired group size here
                    num_groups = num_paragraphs // desired_group_size  # Calculate the number of groups based on desired group size
                    groups = [paragraphs[i:i + desired_group_size] for i in range(0, len(paragraphs), desired_group_size)]
                    story = ""
                    for paragraph in paragraphs:
                        story += paragraph.text + "\n"
                    story = story.replace('<p>', '')
                    story = story.replace('"', '')
                    
                    st.markdown("""<style>
                          .stMarkdown{color: black;}
                          .st-c8:hover{color:orange;}
                          .streamlit-expander.st-bc.st-as.st-ar.st-bd.st-be.st-b8.st-bf.st-bg.st-bh.st-bi{display:none;}
                          </style>""",
                          unsafe_allow_html=True
                    )
                    with st.expander("Read"):
                        from annotated_text import annotated_text
                        paragraphs = story.split("\n") 
                        formatted_paragraphs = [(paragraph, "", "#fea") for paragraph in paragraphs]
                        annotated_text(*formatted_paragraphs)
                        st.caption(f'{len(story)} characters in this chapter.')

                        oldurl = url
                        chap = ''.join([n for n in oldurl if n.isdigit()])
                        nxtchap = str(int(chap) + int(+1))
                        prvchap = str(int(chap))
                        nxtUrl = str(oldurl.replace(chap, nxtchap))
                        obfuscated_text, mapping = obfuscate(nxtUrl)
                        st.caption(":green[Chapter Complete:] " + prvchap + "\n\n:orange[Next Chapter:] " + nxtchap)
                        st.caption(obfuscated_text)
                        url = deobfuscate(obfuscated_text, mapping)
                        st.button('Continue', on_click=readit, args=[url], key=generate_unique_key())
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                        story = story.replace('"','')
                        tts = gTTS(text=story, lang='en', slow=False)
                        tts.save(tmp_file.name)                            
                        audio = AudioSegment.from_mp3(tmp_file.name)
                        new_file = speedup(audio,1.2,150)
                        new_file.export("file.mp3", format="mp3")
                        autoplay_audio("file.mp3")
                        #st.download_button("file.mp3")
                    for group in groups:
                        group_text = ""
                        for d_paragraph in group:
                            group_text += d_paragraph.text + "\n"
                        #if on:
                        #    res_box.markdown(f':blue[Dao: ]:green[*{d_paragraph.text}*]')
                        #    time.sleep(5)
                    driver.quit()
                else:
                    st.write('')
            else:
                st.write(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
        except Exception as e:
            st.write(f':blue[Dao: ]:green[*Error occurred: {e}*]')
    driver.quit()

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
st.set_page_config(
    page_title="Manga Dōjutsu",
    page_icon=icob,
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        <br><hr><center>
        .reportview-container {background: black;}
        .sidebar .siderbar-content {background: black;}
        .st-ck:hover {
        color: #gold;
        }
        color: lime;
        cursor: pointer;
        }
        img {
        width:75%;
        }
        width:578px;
        vertical-align: middle;
        horizontal-align: middle;
        max-width: 300px;
        margin: auto;
        }
        .css-yhwc6k{
        text-align: center;
        }
        #audio{autoplay:true;}
        #MainMenu{visibility: hidden;}
        footer{visibility: hidden;}
        .css-14xtw13 e8zbici0{visibility: hidden;}
        .css-m70y {display:none}
        .st-emotion-cache-zq5wmm.ezrtsby0{visibility: hidden;}
        .st-emotion-cache-zq5wmm.ezrtsby0{display:none}
        .styles_terminalButton__JBj5T{visibility: hidden;}
        .styles_terminalButton__JBj5T{display:none}
        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{visibility: hidden;}
        .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N{display:none}
        [data-testid='stSidebarNav'] > ul {min-height: 50vh;}
        [data-testid='stSidebarNav'] > ul {color: red;}
        .language-java {color: black;}
    </style>
""", unsafe_allow_html=True)

main_image = Image.open('static/dojutsu.png')
side_image = Image.open('static/4.png')
st.sidebar.write('BlackDao: Manga Dōjutsu')

if 'image_links' not in st.session_state:
    st.session_state.image_links = []
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

genre = None

with st.sidebar:
    if 'value' not in st.session_state:
        st.session_state.value = ""
    def update_value():
        st.session_state.value = "Restart"
        
    st.image(side_image)
    st.caption("Manga Text or Image To Speach")
    on = st.checkbox('Stream Story (Disabled)', value=False, disabled=True)

	
    st.divider()
    st.header("Google Play Store")
    st.caption("Download from: https://play.google.com/store/apps/details?id=com.blackbots.blackdao")
    st.header("Official PC Version")
    st.caption("Download from: https://blackbots.gumroad.com/l/manga")
    st.caption("Join Our Discord: https://discord.gg/HcVPaSpF")
    st.divider()
    with st.expander("Help"):
        st.caption("How to use BlackDao: Manga Dōjutsu")
        st.caption("- `Copy` a Code")
        st.caption("- `Paste` Code onto `Manga Code` field")
        st.caption("- `Press Read`")
    st.button("Restart", on_click=update_value, key='keyy')

search_variable = st.text_input(":orange[Search:]", placeholder="Search..", key='search', help="Enter a title here to search for")
                            
if search_variable:
    if '"' in search_variable:
        search_variable = search_variable.replace('"', '')
    with st.spinner('Searching..'):
        with st.expander(":mag: Search"):
            search_url_1 = f"https://daotranslate.us/?s={search_variable}"
            resp_1 = requests.get(search_url_1)
            search_url_2 = f"https://manhuaaz.com/?s={search_variable}&post_type=wp-manga&op=&author=&artist=&release=&adult="
            resp_2 = requests.get(search_url_2)
            
            if resp_1.status_code == 200 and resp_2.status_code == 200:
                soup_1 = BeautifulSoup(resp_1.text, 'html.parser')
                soup_2 = BeautifulSoup(resp_2.text, 'html.parser')
                
                search_result_div_1 = soup_1.find("div", {"class": "listupd"})
                search_result_div_2 = soup_2.find_all("a", href=lambda href: href and href.startswith("https://manhuaaz.com/manga/"))
                
                if search_result_div_1 and search_result_div_2:
                    titles = search_result_div_1.find_all("div", {"class": "mdthumb"})
                    manga_links = iter(search_result_div_2)
                    for title in titles:
                        title_url = title.a["href"]
                        title_name = title_url.split("series/")[1].replace('/', '').title()
                        titlename = title_name.replace('-', ' ')
                        ih = f"https://daotranslate.us/{title_name}-chapter-1/"
                        with st.spinner('Searching..'):
                            st.write(f"[{titlename}]({ih})")
                            img_url = title.img["src"]
                            original_string = ih
                            obfuscated_text, mapping = obfuscate(original_string)
                            if img_url:
                                st.image(img_url, use_column_width='always')
                            if ih:
                                txt = f"""
                                {obfuscated_text}
                                """
                                url = deobfuscate(obfuscated_text, mapping)
                                st.code(txt, language='java')
                                st.button('Read', on_click=readit, args=[url], key=generate_unique_key())
                            st.divider()
                            
                            # Display results from search_result_div_2
                            try:
                                link = next(manga_links)
                                href = link.get("href")
                                if "chapter" not in href:
                                    cch = f"{href}chapter-1/"
                                else:
                                    cch = href
                                manga_name=href.split('https://manhuaaz.com/manga/')[1]
                               
                                img_tag = link.find("img")
                                original_string = cch
                                obfuscated_text, mapping = obfuscate(original_string)
                                if img_tag:
                                    st.write(f"[{manga_name}]({cch})")
                                    img_url = img_tag.get("data-src")
                                    st.image(img_url, caption=obfuscated_text, use_column_width='always')
                                    
                                    txt = f"""
                                    {obfuscated_text}
                                    """
                                    st.code(txt, language='java')
                                    st.caption('Copy Code')
                                    st.divider()
                            except StopIteration:
                                break


col1, col2, col3 = st.columns(3)
outer_cols = st.columns([1, 2])

with col1:
    ranchar = random.choice(string.ascii_uppercase)
    with st.expander(':books: Novels'):
        resp = requests.get(f"https://daotranslate.us/?s={ranchar}")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_list_div = soup.find("div", {"class": "listupd"})
            if manga_list_div:
                titles = manga_list_div.find_all("div", {"class": "mdthumb"})
                for title in titles:
                    title_url = title.a["href"]
                    title_name = title_url.split("series/")[1].replace('/', '').title()
                    titlename = title_name.replace('-', ' ')
                    ch = f"https://daotranslate.us/{title_name}-chapter-1/"
                    st.write(f"[{titlename}]({ch})")
                    img_url = title.img["src"]
                    
                    original_string = ch
                    obfuscated_text, mapping = obfuscate(original_string)
                    if img_url:
                        st.image(img_url, use_column_width='always')
                    if ch:
                        txt = f"""
                        {obfuscated_text}
                        """
                        url = deobfuscate(obfuscated_text, mapping)
                        st.code(txt, language='java')
                        st.button('Read', on_click=readit, args=[url], key=generate_unique_key())
                    st.divider()

with col2:
    with st.expander(f":frame_with_picture: Top Rated"):
        resp = requests.get("https://nightcomic.com/")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_items = soup.find_all("div", class_="page-item-detail manga")
        
            for item in manga_items:
                link = item.find("a", class_="btn-link")
                img_tag = item.find("img")
                title = item.find("h3", class_="h5").text.strip()
                rating = item.find("span", class_="score").text.strip()
                
                if link and img_tag:
                    href = link.get("href")
                    img_url = img_tag.get("data-src")
                    
                    original_string = href
                    obfuscated_text, mapping = obfuscate(original_string)
                    url = deobfuscate(obfuscated_text, mapping)
                    
                    st.write(f"[{title}]({href}) - Rating: {rating}")
                    st.image(img_url, use_column_width='always')
                    txt = f"""
                    {obfuscated_text}
                    """
                    st.code(txt, language='java')
                    st.caption('Copy Code')
                    st.divider()
with col3:
    with st.expander(f":frame_with_picture: Panels"):
        resp = requests.get("https://manhuaaz.com/")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_links = soup.find_all("a", href=lambda href: href and href.startswith("https://manhuaaz.com/manga/"))
        
            for link in manga_links:
                href = link.get("href")
                if "chapter" not in href:
                    cch = f"{href}chapter-1/"
                else:
                    cch = href
                manga_name=href.split('https://manhuaaz.com/manga/')[1]
                
                img_tag = link.find("img")
                original_string = cch
                obfuscated_text, mapping = obfuscate(original_string)
                if img_tag:
                    st.write(f"[{manga_name}]({cch})")
                    img_url = img_tag.get("data-src")
                    st.image(img_url, use_column_width='always')
                    url = deobfuscate(obfuscated_text, mapping)
                    txt = f"""
                    {obfuscated_text}
                    """
                    st.code(txt, language='java')
                    st.caption('Copy Code')
                    st.divider()

st.image(main_image)
res_box = st.empty()

url = deobfuscate(st.text_input(":orange[Manga Code:]", value='', placeholder="iuuqt://ebhdrrghmbuf.vt/..", key='readfield', help="Enter Manga Code here"), mapping)
ok = st.button(":green_book: Read", help="Read", key='readbutton', use_container_width=False)

if ok:
    #url = deobfuscate(xx, mapping)
    if "daotrans" in url:
        with st.spinner('Loading, please be patient..'):
            readit(url)
    if "daotrans" not in url.lower():
        with st.spinner('Loading text & audio..'):
            driver = get_driver()
            if "nightcomic.com" in url.lower():
                st.session_state.image_links = get_image_links2(url)
            else:
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
 
