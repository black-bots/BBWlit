import os
import base64
import tempfile
import time
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.os_manager import ChromeType


st.set_page_config(
    page_title="Manga Dōjutsu",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Selenium configuration
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Initialize webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=options)
# Function to autoplay audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Function to transcribe text to audio
def transcribe_to_audio(text: str):
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(tmp_file.name)
        audio = AudioSegment.from_mp3(tmp_file.name)
        new_audio = speedup(audio, 1.2, 150)
        new_audio.export(tmp_file.name, format='mp3')
        autoplay_audio(tmp_file.name)

main_image = Image.open('static/dojutsu.png')
side_image = Image.open('static/1.png')
st.image(main_image)
res_box = st.empty()

def main():
    st.title("Manga Dōjutsu")

    # Streamlit sidebar layout
    with st.sidebar:
        st.caption("Manga Text or Image To Speech")
	    on = st.checkbox('Stream Story', value=True)
	    
	    col1, col2 = st.columns(2)
	    outer_cols = st.columns([1, 1])
	    with col1:
	        with st.expander("Text Based"):
	            st.caption("Example: https://daotranslate.us/solo-leveling-ragnarok-chapter-1/")
	            with st.expander("Latest Releases"):
	                resp = requests.get("https://daotranslate.us/series/?status=&type=&order=update")
	                if resp.status_code == 200:
	                    soup = BeautifulSoup(resp.text, 'html.parser')
	                    manga_list_div = soup.find("div", {"class": "listupd"})
	                    if manga_list_div:
	                        titles = manga_list_div.find_all("div", {"class": "mdthumb"})
	                        for title in titles:
	                            title_url = title.a["href"]
	                            title_name = title_url.split("series/")[1]
	                            title_name = title_name.replace('/', '')
	                            title_name = title_name.title()
	                            st.write(f"Title: :green[{title_name}]  \nURL: {title_url}\n")
	            with st.expander("Search.."):
	                search_variable = st.text_input(":orange[Title:]", placeholder="Martial Peak", key='search', help="Enter a title here to search for")
	                search_url = f"https://daotranslate.us/?s={search_variable}"
	                resp = requests.get(search_url)
	                if resp.status_code == 200:
	                    soup = BeautifulSoup(resp.text, 'html.parser')
	                    search_result_div = soup.find("div", {"class": "listupd"})
	                    if search_result_div:
	                        titless = search_result_div.find_all("div", {"class": "mdthumb"})
	                        for title in titless:
	                            title_url = title.a["href"]
	                            title_name = title_url.split("series/")[1]
	                            title_name = title_name.replace('/', '')
	                            title_name = title_name.title()
	                            st.write(f"Title: :green[{title_name}]  \nURL: {title_url}\n")
	                            ch = f"https://daotranslate.us/{title_name}-chapter-1/"
	                            st.write(f"CH 01: {ch}")
	    with col2:
	        with st.expander("Image Based"):
	            st.caption("Example: https://manhuaaz.com/manga/monster-pet-evolution/chapter-1/")
	            with st.expander("Latest Releases"):
	                resp = requests.get("https://manhuaaz.com/")
	                if resp.status_code == 200:
	                    soup = BeautifulSoup(resp.text, 'html.parser')
	                    manga_links = soup.find_all("a", href=lambda href: href and href.startswith("https://manhuaaz.com/manga/"))
	                
	                    for link in manga_links:
	                        href = link.get("href")
	                        manga_name = href.split("https://manhuaaz.com/manga/")[1]
	                        ch = f"{href}/chapter-1/"
	                        st.write(f"Title: :green[{manga_name}]  \nCH 01: {ch}\n")
	                        
	            with st.expander("Search.."):
	                search_variable = st.text_input(":orange[Title:]", placeholder="Martial Peak", key='search2', help="Enter a title here to search for")
	                search_url = f"https://manhuaaz.com/?s={search_variable}&post_type=wp-manga"
	                resp = requests.get(search_url)
	                if resp.status_code == 200:
	                    soup = BeautifulSoup(resp.text, 'html.parser')
	                    tab_thumbs = soup.find_all("div", class_="tab-thumb c-image-hover")
	                    for tab_thumb in tab_thumbs:
	                        # Extract title and URL from the anchor tag within the div
	                        title_name = tab_thumb.find("a")['title']
	                        title_url = tab_thumb.find("a")['href']
	                        ch = f"{title_url}chapter-1/"
	                        st.write(f"Title: :green[{title_name}]  \nCH 01: {ch}\n")
	    url = st.text_input(":orange[CH. Url:]", placeholder="https://daotranslate.us/solo-leveling-ragnarok-chapter-1/", key='input', help="Enter manga chapter URL here")
	    ok = st.button("📚Read", help="Read", key='123', use_container_width=False)
	    st.header("Official PC Version")
	    st.caption("Download from: https://blackbots.gumroad.com/l/manga")
	    st.caption("Join Our Discord: https://discord.gg/HcVPaSpF")

    # Streamlit main layout
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.caption("Official PC Version: Download from https://blackbots.gumroad.com/l/manga")
    st.caption("Join Our Discord: https://discord.gg/HcVPaSpF")

    # Streamlit content
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Official PC Version")
    st.caption("Download from: https://blackbots.gumroad.com/l/manga")
    st.caption("Join Our Discord: https://discord.gg/HcVPaSpF")

    # Implement your main content here

# Run the main function
if __name__ == "__main__":
    main()
