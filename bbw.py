# Standard library imports
import os
import base64
import time
import tempfile
from io import BytesIO

# Third-party library imports
import requests
from gtts import gTTS
from PIL import Image

# Streamlit imports
import streamlit as st

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# BeautifulSoup imports
from bs4 import BeautifulSoup

history = []

icob = Image.open('static/-.ico')

st.set_page_config(
    page_title="BlackButler WEB",
    page_icon=icob,
    layout="centered",
    initial_sidebar_state="collapsed"
)

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

st.markdown('\n        <style>\n        <br><hr><center>\n                .embeddedAppMetaInfoBar_container__LZA_B{visibility:hidden;}\n            button:hover {\n                background-color: #3DD56D;\n                transition: all 0.3s ease-in-out;\n            }\n            .st-ck:hover {\n                color: #3DD56D;\n            }\n            .st-c6 {\n                color: #FFBD45;\n            }\n            .st-mh:hover {\n                background-color: #grey;\n                color: gold;\n                border: 2px solid #FFBD45;\n                box-shadow: 0 0 10px #FFBD45;\n                transition: all 0.3s ease-in-out;\n                border-color: #FFBD45;\n                cursor: pointer;\n            }\n            .st-mh{\n                border-color: #FFBD45;\n            }\n            .st-cp {\n                background-color: #FFBD45);\n                border-color: #3DD56D;\n            }\n            .css-1f1kxg3{\n                border-color: #FFBD45;\n            }\n            .css-5uatcg{\n                border-color: #FFBD45;\n            }\n            .css-z09lfk{\n                border-color: #FFBD45;\n            }\n            .st-e9{\n                background: #FFBD45;\n            }\n            .st-co{\n                color: white;\n            }\n            .css-10y5sf6{\n                color: #FFBD45;\n            }\n            .css-demzbm{\n                background-color: #FFBD45;\n            }\n            .st-hp {\n                background-color: #FFBD45);\n            }\n\n            .st-ju{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 1%, #000000 1%);\n            }\n            .st-li{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 10%, #000000 10%);\n            }\n            .st-lh{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 20%, #000000 20%);\n            }\n            .st-lg{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 35%, #000000 30%);\n            }\n            .st-lf{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 35%, #000000 50%);\n            }\n            .st-le{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 45%, #000000 60%);\n            }\n            .st-ld{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 55%, #000000 70%);\n            }\n            .st-lj{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 65%, #000000 80%);\n            }\n            .st-lk{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 80%, #000000 90%);\n            }\n            .st-ll{\n                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 100%, #000000 100%);\n            }\n            img {\n                width:50%;\n            }\n            .css-1v0mbdj{\n                width:578px;\n                vertical-align: middle;\n                horizontal-align: middle;\n                max-width: 300px;\n                margin: auto;\n            }\n            .css-yhwc6k{\n            text-align: center;\n            }\n\t    #audio{autoplay:true;}\n                #MainMenu{visibility: hidden;}\n                footer{visibility: hidden;}\n                .css-14xtw13 e8zbici0{visibility: hidden;}</style>',unsafe_allow_html=_A)

@st.cache_resource
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

driver = get_driver()

res_box = st.empty()
tab1,tab2=st.tabs(['Text Based','Image Based'])
with tab1:
    with st.expander("Need a link?"):
        st.caption("ex: https://daotranslate.us/absolute-necromancer-chapter-1/")
    url = st.text_input(":orange[CH. Url:]", placeholder="https://daotranslate.us/absolute-necromancer-chapter-1/", key='input', help="Enter manga chapter here")
    ok = st.button("📚", help="Read", key='123', use_container_width=False)
    
    res_box.markdown(f':blue[Dao: Ready to read!]')
    
    if ok:
        manga = driver.get(url)
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
                        story = story.replace('<p>', '').replace('</p>', '')
                        
                        # Convert text to speech and save it as a temporary mp3 file
                        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                            tts = gTTS(text=story, lang='en', slow=False)
                            tts.save(tmp_file.name)                            

                            autoplay_audio(tmp_file.name)
                            
                        with st.expander("Read"):
                            st.write(f':green[*{story}*]')

                        for group in groups:
                            group_text = ""
                            for d_paragraph in group:
                                group_text += d_paragraph.text + "\n"
                            res_box.markdown(f':blue[Dao: ]:green[*{group_text}*]')
                            time.sleep(3)
                        next_ch = st.button("Next CH.", key='next_button', help="Next Chapter", use_container_width=False)
                        if next_ch:
                            oldurl = url
                            chap = ''.join([n for n in oldurl if n.isdigit()])
                            nxtchap = str(int(chap) + int(+1))
                            prvchap = str(int(chap))
                            nxtUrl = str(oldurl.replace(chap, nxtchap))
                            st.caption("Chapter Complete: " + prvchap + "\n\nNEXT CHAPTER\nChapter: " + nxtchap, text_color='orange')

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
                                    story = story.replace('<p>', '').replace('</p>', '')
                                    
                                    # Convert text to speech and save it as a temporary mp3 file
                                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                                        tts = gTTS(text=story, lang='en', slow=False)
                                        tts.save(tmp_file.name)                            
            
                                        autoplay_audio(tmp_file.name)
                                        
                                    with exapnder("Read"):
                                        st.write(f':green[*{story}*]')
            
                                    for group in groups:
                                        group_text = ""
                                        for d_paragraph in group:
                                            group_text += d_paragraph.text + "\n"
                                        res_box.markdown(f':blue[Dao: ]:green[*{group_text}*]')
                                        time.sleep(3)
                                    next_ch = st.button("Next CH.", key='next_button', help="Next Chapter", use_container_width=False)
                                    if next_ch:
                                        oldurl = url
                                        chap = ''.join([n for n in oldurl if n.isdigit()])
                                        nxtchap = str(int(chap) + int(+1))
                                        prvchap = str(int(chap))
                                        nxtUrl = str(oldurl.replace(chap, nxtchap))
                                        st.caption("Chapter Complete: " + prvchap + "\n\nNEXT CHAPTER\nChapter: " + nxtchap, text_color='orange')        
                            
                    else:
                        res_box.markdown(f':blue[Dao: ]:green[*No manga content found at the provided URL.*]')
                else:
                    res_box.markdown(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
            except Exception as e:
                res_box.markdown(f':blue[Dao: ]:green[*Error occurred: {e}*]')
                        
        st.markdown("____________________________________________________________")
        
session_state = st.session_state

# Function to get image links from the provided URL
def get_image_links(url):
    driver.get(url)
    time.sleep(5)

    image_links = []

    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

    for img_element in img_elements:
        img_src = img_element.get_attribute('src')

        if img_src:
            image_links.append(img_src)

    return image_links

# Function to filter out non-image links
def is_image_link(link):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg']
    for ext in image_extensions:
        if link.lower().endswith(ext):
            return True
    return False

# Function to get image links from the provided URL
def get_image_links(url):
    driver.get(url)
    time.sleep(5)

    image_links = []

    img_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

    for img_element in img_elements:
        img_src = img_element.get_attribute('src')

        if img_src and is_image_link(img_src):
            image_links.append(img_src)

    return image_links

with tab2:
    with st.expander("Need a link?"):
        st.caption("ex: https://mangapark.io/title/248099-en-plunder-the-sky/8455452-ch-001")
    url = st.text_input(":orange[CH. Url:]", placeholder="https://mangapark.io/title/248099-en-plunder-the-sky/8473991-ch-042", key='inputt', help="Enter manga chapter here")
    okk = st.button("🖼️", help="Read", key='1223', use_container_width=False)

    if okk:
        session_state.image_links = get_image_links(url)
        session_state.current_image_index = 0

        if session_state.image_links:
            st.image(session_state.image_links[0], use_column_width=True)

        st.write(f"Total Images: {len(session_state.image_links)}")

    try:
        if session_state.image_links:
            next_button_clicked = st.button("Next", key='next_button', help="Show next image", use_container_width=False)
    
            if next_button_clicked:
                session_state.current_image_index += 1
                if session_state.current_image_index >= len(session_state.image_links):
                    session_state.current_image_index = 0
                st.image(session_state.image_links[session_state.current_image_index], use_column_width=True)
    except:
        pass

st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
