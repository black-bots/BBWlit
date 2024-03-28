# Copyright 2023 Cloud Bots™
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "BlackBots"
__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"
__credits__ = ["Supreme Ciento"]
__license__ = "GPL"
__maintainer__ = "Cloud Bots™ BlackBots"
__email__ = "admin@blackbots.com"
__status__ = "Production"

__version__ = "8.12.21.0"


import os
import requests
import streamlit as st
from PIL import Image
#import g4f
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

history = []
@st.cache_resource
def get_driver():
    return webdriver.Chrome(
	service=Service(
	    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
	),
	options=options,
)
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = get_driver()
def air(prompt):
	model_prompt = """
			You are CommBot, and write Instagram posts & hashtags restricted in size by the platform.
			Output one to three sentences. Do not label the output sections, just write the contents: {}
	""".format(prompt)
	
	response = g4f.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": model_prompt}],
		stream=False,
		n=1,
		stop=None,
		temperature=0.3,
	)
	
	return response
            
icob = Image.open('static/-.ico')

st.set_page_config(
    page_title="BlackButler WEB",
    page_icon=icob,
    layout="centered",
    initial_sidebar_state="collapsed"
)

bottom_image=Image.open('static/1.png')
top_image=Image.open('static/4.png')
_image=Image.open('static/3.png')
st.markdown("""
        <style>
        <br><hr><center>
            button:hover {
                background-color: #3DD56D;
                transition: all 0.3s ease-in-out;
            }
            .st-ck:hover {
                color: #3DD56D;
            }
            .st-c6 {
                color: #FFBD45;
            }
            .st-mh:hover {
                background-color: #grey;
                color: gold;
                border: 2px solid #FFBD45;
                box-shadow: 0 0 10px #FFBD45;
                transition: all 0.3s ease-in-out;
                border-color: #FFBD45;
                cursor: pointer;
            }
            .st-mh{
                border-color: #FFBD45;
            }
            .st-cp {
                background-color: #FFBD45);
                border-color: #3DD56D;
            }
            .css-1f1kxg3{
                border-color: #FFBD45;
            }
            .css-5uatcg{
                border-color: #FFBD45;
            }
            .css-z09lfk{
                border-color: #FFBD45;
            }
            .st-e9{
                background: #FFBD45;
            }
            .st-co{
                color: white;
            }
            .css-10y5sf6{
                color: #FFBD45;
            }
            .css-demzbm{
                background-color: #FFBD45;
            }
            .st-hp {
                background-color: #FFBD45);
            }

            .st-ju{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 1%, #000000 1%);
            }
            .st-li{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 10%, #000000 10%);
            }
            .st-lh{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 20%, #000000 20%);
            }
            .st-lg{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 35%, #000000 30%);
            }
            .st-lf{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 35%, #000000 50%);
            }
            .st-le{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 45%, #000000 60%);
            }
            .st-ld{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 55%, #000000 70%);
            }
            .st-lj{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 65%, #000000 80%);
            }
            .st-lk{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 80%, #000000 90%);
            }
            .st-ll{
                background: linear-gradient(to right, rgba(255, 189, 69, 0.25) 0%, rgba(255, 189, 69) 100%, #000000 100%);
            }
            img {
                width:50%;
            }
            .css-1v0mbdj{
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
            .embeddedAppMetaInfoBar_container__LZA_B{visibility:hidden;}
            button:hover {
                    background-color: #3DD56D; 
                    transition: all 0.3s ease-in-out;
            }

        </style>
    """,
    unsafe_allow_html=True
    )

#with tab1:
res_box = st.empty()

#############################################################################
text = st.text_area(":orange[Say or Ask something]", key='input', help="Type your message here")
ok = st.button("📩", help="Send Message", key='123', use_container_width=False)

res_box.markdown(f':blue[BlackButler:  ]')

if ok:
	driver.get("https://black-bots-bbwlit-bbw-cdngjf.streamlit.app/")
	
	st.code(driver.page_source)
	#result =air(text)
	res_box.markdown(f':blue[BlackButler:  ]:green[*{result}*]')				
	st.markdown(f':blue[BlackButler:  ]:green[*{result}*]')				
	
	st.download_button('Save Response', result,key="847*")
	st.markdown("----")

else:
    print('')



st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
