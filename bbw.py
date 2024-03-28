import os
import requests
from bs4 import BeautifulSoup
import streamlit as st
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

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

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

driver = get_driver()

res_box = st.empty()

url = st.text_input(":orange[CH. Url:]", key='input', help="Enter manga chapter here")
ok = st.button("📩", help="Read", key='123', use_container_width=False)

res_box.markdown(f':blue[BlackButler: ]')

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

                    for group in groups:
                        group_text = ""
                        for d_paragraph in group:
                            group_text += d_paragraph.text + "\n"
                            finished = False
                            while not finished:
                                res_box.markdown(f':blue[BlackButler: ]:green[*{group_text}*]')
                                finished = True
                                if finished is True:
                                    break
                else:
                    res_box.markdown(f':blue[Dao: ]:green[*No manga content found at the provided URL.*]')
            else:
                res_box.markdown(f':blue[Dao: ]:green[*Failed to fetch URL. Check your internet connection or the validity of the URL.*]')
        except Exception as e:
            res_box.markdown(f':blue[Dao: ]:green[*Error occurred: {e}*]')
    st.code(group_text)
    st.download_button('Download Text', group_text, key="847*")
    st.markdown("____________________________________________________________")

st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
