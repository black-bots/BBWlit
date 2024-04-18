# ┌──────────────────────────────────┐
# │ BlackGram - Manga Dōjutsu v1.23  │
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
import base64
import time
import random
import tempfile
import io
from io import BytesIO
import uuid
import hashlib

import re
import requests
from pydub import AudioSegment
from pydub.effects import speedup
from gtts import gTTS
from PIL import Image

import easyocr as ocr  # OCR
import numpy as np  # Image Processing
from easyocr import Reader
import streamlit as st
import streamlit_nested_layout
import streamlit.components.v1 as components
from streamlit_extras.beta_expander import beta_expander

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from bs4 import BeautifulSoup
import webbrowser


def generate_unique_key():
    unique_id = str(uuid.uuid4())
    hashed_key = hashlib.sha256(unique_id.encode()).hexdigest()
    return hashed_key

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

def transcribe_to_audio(image_links):
    audio_files = []
    for idx, img_link in enumerate(image_links, start=1):
        try:
            if not is_supported_image_format(img_link):
                # st.write(f"Skipping image {img_link} as it is not in a supported format.")
                continue

            with st.spinner(" Getting image text "):
                reader = ocr.Reader(['en'])
                result = reader.readtext(img_link)
                result_text = []  # empty list for results
                for text in result:
                    result_text.append(text[1].strip())

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
        except Exception as e:
            st.write(f"Error processing {img_link}: {e}")
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

#@st.cache_resource
def load_model() -> Reader:
    return ocr.Reader(["en"], model_storage_directory=".")

def filter_english_words(text):
    english_word_pattern = r'\b[a-zA-Z]+(?:\'[a-zA-Z]+)?(?:-[a-zA-Z]+)?(?:[.,!?\'":;\[\]()*&^%$#@`~\\/]|\.\.\.)?\b'
    english_words = re.findall(english_word_pattern, text)
    english_text = ' '.join(english_words)
    text = english_text.lower()
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
                        st.caption(":green[Chapter Complete:] " + prvchap + "\n\n:orange[Next Chapter:] " + nxtUrl)
                        txt = st.text_area(
                            "Link",
                            f"{nxtUrl}",
                            key=generate_unique_key())
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
        [data-testid='stSidebarNav'] > ul {
            min-height: 50vh;
        }
        [data-testid='stSidebarNav'] > ul {
            color: red;
        }
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

main_image = Image.open('static/dojutsu.png')
side_image = Image.open('static/4.png')
st.sidebar.write('BlackDao: Manga Dōjutsu')

if 'image_links' not in st.session_state:
    st.session_state.image_links = []
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

genre = None

with st.sidebar:
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
        st.caption("- Enter search term into field to search Mangas")
        st.caption("- Copy & Paste link into input field on main window then press Read")
        st.caption("- View Image Based Links with the Image Based Tab")

col1, col2, col3 = st.columns(3)
outer_cols = st.columns([1, 3])

expander =  st.beta_expander("Adjust settings")
expander.write("Test")
if expander.button("Reset Draft"):
    st.write('Draft resetted')

with col1:
    with st.expander(":books: Random"):
        resp = requests.get("https://daotranslate.us/?s=i")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_list_div = soup.find("div", {"class": "listupd"})
            if manga_list_div:
                titles = manga_list_div.find_all("div", {"class": "mdthumb"})
                for title in titles:
                    title_url = title.a["href"]
                    title_name = title_url.split("series/")[1].replace('/', '').title()
                    ch = f"https://daotranslate.us/{title_name}-chapter-1/"
                    
                    st.write(f"[{title_name}]({ch})")
                    img_url = title.img["src"]
                    if img_url:
                        st.image(img_url, caption=ch, use_column_width='always')
                        
                    url = ch
                    submed = st.button("Play:loud_sound:", key=generate_unique_key())  # Fix: Button for text-based content
                    if submed:
                        try:
                            driver.quit()
                        except:
                            pass
                        with st.spinner('Loading text & audio..'):
                            driver = get_driver()
                            driver.get(url)
                    
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
                                            
                                            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                                                story = story.replace('"','')
                                                tts = gTTS(text=story, lang='en', slow=False)
                                                tts.save(tmp_file.name)                            
                                                audio = AudioSegment.from_mp3(tmp_file.name)
                                                new_file = speedup(audio,1.2,150)
                                                new_file.export("file.mp3", format="mp3")
                                                autoplay_audio("file.mp3")
                                                #st.download_button("file.mp3")
                                        
                                            driver.quit()
                                        else:
                                            st.write('')
                                    else:
                                        st.write(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
                                except Exception as e:
                                    st.write(f':blue[Dao: ]:green[*Error occurred: {e}*]')
                            driver.quit()
                    st.divider()
with col2:        
    with st.expander(":frame_with_picture: Image"):
        resp = requests.get("https://manhuaaz.com/")
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            manga_links = soup.find_all("a", href=lambda href: href and href.startswith("https://manhuaaz.com/manga/"))
            for link in manga_links:
                href = link.get("href")
                manga_name = href.split("https://manhuaaz.com/manga/")[1]
                if "chapter" not in manga_name.lower():
                    cch = f"{href}chapter-1/"
                else:
                    cch = href
                st.write(f"[{manga_name}]({cch})")
                img_tag = link.find("img")
                if img_tag:
                    img_url = img_tag.get("data-src")
                    st.image(img_url, caption=cch, use_column_width='always')
                if cch:
                    txt = st.text_area(
                        "Link",
                        f"{cch}",
                        key=generate_unique_key())
                st.divider()
with col3:
    with st.expander(":mag: Search"):
        search_variable = st.text_input(":orange[Search:]", placeholder="", key='search', help="Enter a title here to search for")
        if search_variable:
            search_url = f"https://daotranslate.us/?s={search_variable}"
            resp = requests.get(search_url)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                search_result_div = soup.find("div", {"class": "listupd"})
                if search_result_div:
                    titles = search_result_div.find_all("div", {"class": "mdthumb"})
            
                    for title in titles:
                        title_url = title.a["href"]
                        title_name = title_url.split("series/")[1].replace('/', '').title()
                        ih = f"https://daotranslate.us/{title_name}-chapter-1/"
                        with st.spinner('Searching..'):
                            st.write(f"[{title_name}]({ih})")
                            img_url = title.img["src"]
                            if img_url:
                                st.image(img_url, caption=ih)
                        url = ih
                        submitted = st.button("Play:loud_sound:", key=generate_unique_key())
                        if submitted:
                            try:
                                driver.quit()
                            except:
                                pass
                            with st.spinner('Loading text & audio..'):
                                
                                driver = get_driver()
                                driver.get(url)

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
                                                
                                                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                                                    story = story.replace('"','')
                                                    tts = gTTS(text=story, lang='en', slow=False)
                                                    tts.save(tmp_file.name)                            
                                                    audio = AudioSegment.from_mp3(tmp_file.name)
                                                    new_file = speedup(audio,1.2,150)
                                                    new_file.export("file.mp3", format="mp3")
                                                    autoplay_audio("file.mp3")
                                                    #st.download_button("file.mp3")
                            
                                                driver.quit()
                                            else:
                                                st.write('')
                                        else:
                                            st.write(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
                                    except Exception as e:
                                        st.write(f':blue[Dao: ]:green[*Error occurred: {e}*]')
                                driver.quit()
                    st.divider()
                            
st.image(main_image)
res_box = st.empty()

xx = st.text_input(":orange[Enter Link:]", value='', placeholder="https://daotranslate.us/solo-leveling-ragnarok-chapter-1/", key='readfield', help="Enter manga chapter URL here")

ok = st.button(":green_book: Read", help="Read", key='readbutton', use_container_width=False)
    
tab1,tab2=st.tabs(['Text Based','Image Based'])

with tab1:                  
    if "daotrans" in xx:
        if ok:
            with st.spinner('Loading text & audio..'):
                readit(xx)

with tab2:
    if "daotrans" not in xx.lower():
        if tab2:
            if ok:
                with st.spinner('Loading text & audio..'):
                    st.session_state.image_links = get_image_links(url)
                    st.session_state.current_image_index = 0
            
                    if st.session_state.image_links:
                        for image_link in st.session_state.image_links:
                            st.image(image_link, use_column_width=True)
            
                        st.write(f"Total Images: {len(st.session_state.image_links)}")
            
                        transcribe_to_audio(st.session_state.image_links)
 
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved.  <a href='mailto:admin@blackbots.net?subject=MangaDojutsu!&body=Please specify the issue you are facing with the app.'><strong>BlackBots.net</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
