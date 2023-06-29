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
from bardapi import Bard


os.environ['_BARD_API_KEY'] = 'XQjnNMzBnXOMYBEOJLu5wPojuZhWgMriCO46knG8HAZlFMWaII5_qu3QdhHFRSMEmBsDYw.'
token='XQjnNMzBnXOMYBEOJLu5wPojuZhWgMriCO46knG8HAZlFMWaII5_qu3QdhHFRSMEmBsDYw.'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 

bard = Bard(token=token, session=session, timeout=30)

history = []
from PIL import Image
icob = Image.open('static/-.ico')

st.set_page_config(
    page_title="BlackButler WEB",
    page_icon=icob,
    layout="centered",
    initial_sidebar_state="auto"
)


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

    result = bard.get_answer(text)['content']
    res_box.markdown(f':blue[BlackButler:  ]:green[*{result}*]')				

    st.download_button('Save Response', result,key="847*")
    st.markdown("----")

else:
    print('')



st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
