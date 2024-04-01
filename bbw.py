import os
import base64
import time
import tempfile
from io import BytesIO

import re
import requests
from gtts import gTTS
from PIL import Image

import easyocr as ocr  # OCR
import numpy as np  # Image Processing
from easyocr import Reader
import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from bs4 import BeautifulSoup

history = []

icob = Image.open('static/-.ico')

st.set_page_config(
    page_title="BlackButler WEB",
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
    </style>
""", unsafe_allow_html=True)


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

def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )
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

main_image = Image.open('static/dojutsu.png')
side_image = Image.open('static/1.png')
st.image(main_image)
res_box = st.empty()

with st.sidebar:
    st.image(side_image)
    on = st.checkbox('Stream Story', value=True)
    with st.expander("Need a link?"):
        st.caption("Test Based: https://daotranslate.us/solo-leveling-ragnarok-chapter-1/")
        st.caption("Image Based: https://manhuaaz.com/manga/monster-pet-evolution/chapter-1/")
    url = st.text_input(":orange[CH. Url:]", placeholder="https://daotranslate.us/solo-leveling-ragnarok-chapter-1/", key='input', help="Enter manga chapter here")
    ok = st.button("📚Read", help="Read", key='123', use_container_width=False)
    st.header("Official Version")
    st.caption("Download from: https://blackbots.gumroad.com/l/manga")

tab1,tab2=st.tabs(['Text Based','Image Based'])
with tab1:    
    res_box.markdown(f':blue[Dao:]')
    if tab1:
        if ok:
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
                            num_groups = 100
                            group_size = len(paragraphs) // num_groups
                            groups = [paragraphs[i:i + group_size] for i in range(0, len(paragraphs), group_size)]
        
                            story = ""
                            for paragraph in paragraphs:
                                story += paragraph.text + "\n\n"
                            story = story.replace('<p>', '')
                            story = story.replace('"', '')
                            
                            # Convert text to speech and save it as a temporary mp3 file
                            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                                tts = gTTS(text=story, lang='en', slow=False)
                                tts.save(tmp_file.name)                            
    
                                autoplay_audio(tmp_file.name)
                                
                            with st.expander("Read"):
                                st.write(f':green[*{story}*]')
    
                            if on:
                                for group in groups:
                                    group_text = ""
                                    for d_paragraph in group:
                                        group_text += d_paragraph.text + "\n"
                                    #res_box.markdown(f':blue[Dao: ]:green[*{group_text}*]')
                                    res_box.markdown(f':blue[Dao: ]:green[*{d_paragraph.text}*]')
                                    time.sleep(5)
                            next_ch = st.button("Next CH.", key='next_button', help="Next Chapter", use_container_width=False)
                            if next_ch:
                                oldurl = url
                                chap = ''.join([n for n in oldurl if n.isdigit()])
                                nxtchap = str(int(chap) + int(+1))
                                prvchap = str(int(chap))
                                nxtUrl = str(oldurl.replace(chap, nxtchap))
                                st.caption("Chapter Complete: " + prvchap + "\n\nNEXT CHAPTER\nChapter: " + nxtchap, text_color='orange')                            
                        else:
                            res_box.markdown(f':blue[Dao: ]: ...')
                    else:
                        res_box.markdown(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
                except Exception as e:
                    res_box.markdown(f':blue[Dao: ]:green[*Error occurred: {e}*]')
                            
def get_image_links(url):
    try:
        driver.get(url)
    except WebDriverException as ex:
        if driver.current_url == url:
            st.write('Cannot load the URL..')
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

def transcribe_to_audio(image_links):
    audio_files = []
    for idx, img_link in enumerate(image_links, start=1):
        try:
            img_data = requests.get(img_link).content
            img = Image.open(BytesIO(img_data))
            gray_image = img.convert('L')
            np_image = np.array(gray_image)
            
            with st.spinner(" Getting image text "):
                #reader = load_model()  # load model
                reader = ocr.Reader(['en'])
                result = reader.readtext(np_image)
                #preprocessed_image = cv2.medianBlur(result, 3)
                result_text = []  # empty list for results
                for text in result:
                    result_text.append(text[1].strip())
                    st.write(result_text)

            text = filter_english_words(result_text)

            if text:
                audio_file_path = os.path.join('audio', os.path.splitext(os.path.basename(img_link))[0] + '.mp3')
                if not os.path.exists(audio_file_path):
                    tts = gTTS(text=text, lang='en', slow=False)
                    tts.save(audio_file_path)
                audio_files.append(audio_file_path)
                res_box.markdown(f':blue[RAWR: ]:green[*{text}*]')
            else:
                res_box.markdown(f':blue[Dao: ]:orange[No Text]')
        except Exception as e:
            st.write(f"Error processing {img_link}: {e}")
    return audio_files

def is_image_link(link):
    image_extensions = ['.png', '.jpg', '.jpeg']
    for ext in image_extensions:
        if link.lower().endswith(ext):
            return True
    return False

if 'image_links' not in st.session_state:
    st.session_state.image_links = []
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0
    
@st.cache_resource
def load_model() -> Reader:
    return ocr.Reader(["en"], model_storage_directory=".")

def filter_english_words(text):
    english_word_pattern = r'\b[a-zA-Z]+(?:\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\'":;\[\]()*&^%$#@`~\\/]|\.\.\.)?\b'
    english_words = re.findall(english_word_pattern, text)
    english_text = ' '.join(english_words)
    text = english_text.lower()
    return text

with tab2:
    if tab2:
        if ok:
            st.session_state.image_links = get_image_links(url)
            st.session_state.current_image_index = 0
    
            if st.session_state.image_links:
                st.image(st.session_state.image_links[0], use_column_width=True)
    
            st.write(f"Total Images: {len(st.session_state.image_links)}")
    
        try:
            if st.session_state.image_links:
                transcribe_to_audio(st.session_state.image_links)
                next_button_clicked = st.button("Next", key='next_button', help="Show next image", use_container_width=False)
                if next_button_clicked:
                    st.session_state.current_image_index += 1
                    if st.session_state.current_image_index >= len(st.session_state.image_links):
                        st.session_state.current_image_index = 0
                    st.image(st.session_state.image_links[st.session_state.current_image_index], use_column_width=True)
                    transcribe_to_audio(st.session_state.image_links)
        except:
            pass
 
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
