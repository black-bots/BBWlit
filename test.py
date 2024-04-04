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
from selenium.webdriver.chrome.service import Service
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),options=chrome_options)
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
        st.markdown("<br><hr>", unsafe_allow_html=True)
        st.header("Official PC Version")
        st.caption("Download from: https://blackbots.gumroad.com/l/manga")
        st.caption("Join Our Discord: https://discord.gg/HcVPaSpF")

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
                                    #st.write(f':green[*{story}*]')
                                
                                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                                    story = story.replace('"','')
                                    tts = gTTS(text=story, lang='en', slow=False)
                                    tts.save(tmp_file.name)                            
                                    audio = AudioSegment.from_mp3(tmp_file.name)
                                    new_file = speedup(audio,1.2,150)
                                    new_file.export("file.mp3", format="mp3")
                                    autoplay_audio("file.mp3")
    
                                for group in groups:
                                    group_text = ""
                                    for d_paragraph in group:
                                        group_text += d_paragraph.text + "\n"
                                    if on:
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
        if ok:
            st.session_state.image_links = get_image_links(url)
            st.session_state.current_image_index = 0
    
            if st.session_state.image_links:
                st.image(st.session_state.image_links[0], use_column_width=True)
    
            st.write(f"Total Images: {len(st.session_state.image_links)}")
    
            try:
                if st.session_state.image_links:
                    current_image_index = st.session_state.current_image_index
                    current_image_link = st.session_state.image_links[current_image_index]
                    st.image(current_image_link, use_column_width=True)
    
                    next_button_clicked = st.button("Next", key='next_button', help="Show next image", use_container_width=False)
                    if next_button_clicked:
                        current_image_index += 1
                        if current_image_index >= len(st.session_state.image_links):
                            current_image_index = 0
                        st.session_state.current_image_index = current_image_index
                        current_image_link = st.session_state.image_links[current_image_index]
                        st.image(current_image_link, use_column_width=True)
                        
                        # Transcribe text only for the currently displayed image
                        transcribe_to_audio([current_image_link])
                        
            except Exception as e:
                st.write(f"Error: {e}")
     
    st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
# Run the main function
if __name__ == "__main__":
    main()
