#!/usr/bin/env python

# -*- coding: utf-8 -*-

__author__ = "BlackBots"

__copyright__ = "Copyright 2023, Cloud Bots™ BlackBots"

__credits__ = ["Supreme Ciento"]

__license__ = "GPL"

__maintainer__ = "Cloud Bots™ BlackBots"

__email__ = "admin@blackbots.com"

__status__ = "Production"

__version__ = "12.21.21.0"

import os
import io
import sys
import requests
import streamlit as st
import openai
import datetime
import time
from time import sleep
from threading import Thread
import prompt_toolkit
import PyPDF2
import tempfile
import base64
import json
from PIL import Image
from gtts import gTTS
from io import BytesIO

history = []

icob = Image.open('static/-.ico')

st.set_page_config(

    page_title="Bellatrix",

    page_icon=icob,

    layout="centered",

    initial_sidebar_state="auto"

)

main_image = Image.open('static/-.ico')
top_image = Image.open('static/quillbook.png')
_image = 'static/quill.png'

tree = 'tl.LdEL9R1VSFTnrlnNjWTYU4CmclGKT1URio{qE6l2pY71X{q6'

def deobfuscate(text): 

    result = "" 

    for letter in text: 

        result += chr(ord(letter) - 1) 

    return result


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

	    #audio{autoplay:true;}        </style>

    """,

    unsafe_allow_html=True

    )

    #RGB: 255, 189, 69 RGBA: 255, 189, 69, 1

def Rec():

    Rec = st.button("🎤 Speak", help="Speak to Bellatrix", disabled=True, key='3213', use_container_width=True)

openai.api_key = deobfuscate(tree)

def imagy():

    from bs4 import BeautifulSoup

    from PIL import Image

    import re

    

    ok = st.button("🔎", help="Send Message", key='1023', use_container_width=False)

    if ok:

        r = requests.get("https://www.bing.com/images/search?q="+search)

        soup = BeautifulSoup(r.text, "html.parser")

        d=soup.find("div",{"class":"cico"})

        first_image = d.find("img")

        if first_image:

            searched = first_image['src']

            searched = re.sub('42', '512', searched)

        else:

            st.write("Couldn't find image results!")

        image = searched

        st.image(image, caption='Image found with Bing')

def AiMG():

    @st.cache_data(persist=True,show_spinner=False)

    def openai_image(prompt):

        response = openai.Image.create(

          prompt=prompt,

          n=1,

          size="256x256"

        )

        image_url = response['data'][0]['url']

        return image_url

    input_text = st.text_area(":orange[Enter text here... 🙋]",height=50)

    image_button = st.button("Generate Image 🚀")

    if image_button and input_text.strip() != "":

        with st.spinner("Loading...💫"):

            image_url = openai_image(input_text)

            st.image(image_url, caption='Generated by Ai')

###############################

st.image(_image,use_column_width="auto")


with st.sidebar:

	st.image(top_image,use_column_width=True)

	st.info('Settings', icon="ℹ️")

	dropdown_menu = st.selectbox(

		'Set Tone',

		('Bellatrix','Neutral','Assertive','Cooperative','Curious','Encouraging','Formal','Friendly','Informal','Optimistic','Pessimistic','Sincere','Surprised','Worried'),help="Select writing tone")

	Genre = st.text_input('What genre are we writing about?','Fiction', help="Writing Genre")
	selected2 = st.checkbox('Speak responses?', value=True,help="Speak reponses out-loud")

	selected = st.checkbox('Stream responses?', value=True,help="Stream reponses in real-time")

	slider_value = st.slider(':orange[Response style]', 0.1, 1.0, 0.70, step=0.10,help="Set the personality of the Ai (0.10 Predicatble - 1.00 Creative)")

	if dropdown_menu == 'Bellatrix':
		
		st.write(':orange[Tone: ]:green[ Set]')

		prompto = "You will write with a sassy tone"

	elif dropdown_menu == 'Neutral':

		st.write(':orange[Tone: ]:green[ Set]')

		prompto = "You will write with a neutral tone"

	slider = slider_value


res_box = st.empty()
#############################################################################

user_input = st.text_area(":orange[What should we write about?]", "ie: 'Start writing a science fiction novel about Vampires' - Write Here", help="Type what you want to write about",key="placeholder")

def Col():
	col1, col2, col3, col4 = st.columns(4)
	with col1:
		Rewrite = st.button("Rewrite", help="Rewrite", key='996', use_container_width=False)

		if Rewrite:
			report = []
			for resp in openai.Completion.create(model='text-davinci-003',
							prompt="Rewrite this, " + user_input + ", using a" + dropdown_menu + " tone:",
							max_tokens=1012, 
							temperature = slider,
							stream = True):
					report.append(resp.choices[0].text)
					result = "".join(report).strip()
					result = result.replace("\n", "")
					res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

			if Rewrite & selected2:
				speech = BytesIO()
				speech_ = gTTS(
					text=result, 
					lang='en', 
					slow=False
				)
				speech_.write_to_fp(speech)
				st.audio(speech)				
			st.download_button('Save Response', result,key="847*")


	with col2:
		Summarize = st.button("Summarize", help="Summarize", key='994', use_container_width=False)
		if Summarize:
			report = []
			for resp in openai.Completion.create(model='text-davinci-003',
							prompt="Summarize this, " + user_input + ", using a" + dropdown_menu + " tone:",
							max_tokens=1012, 
							temperature = slider,
							stream = True):
					report.append(resp.choices[0].text)
					result = "".join(report).strip()
					result = result.replace("\n", "")
					res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

			if Rewrite & selected2:
				speech = BytesIO()
				speech_ = gTTS(
					text=result, 
					lang='en', 
					slow=False
				)
				speech_.write_to_fp(speech)
				st.audio(speech)				
			st.download_button('Save Response', result,key="847*")
	with col3:
		Brainstorm = st.button("Brainstorm", help="Summarize", key='992', use_container_width=False)
		if Brainstorm:
			report = []
			for resp in openai.Completion.create(model='text-davinci-003',
							prompt="Brainstorm and create a list of 10-20 creative writing ideas.",
							max_tokens=1012, 
							temperature = slider,
							stream = True):
					report.append(resp.choices[0].text)
					result = "".join(report).strip()
					result = result.replace("\n", "")
					res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

			if Rewrite & selected2:
				speech = BytesIO()
				speech_ = gTTS(
					text=result, 
					lang='en', 
					slow=False
				)
				speech_.write_to_fp(speech)
				st.audio(speech)				
			st.download_button('Save Response', result,key="847*")		
	with col4:
		Title = st.button("Create Title", help="Create Titles", key='990', use_container_width=False)
		if Title:
			report = []
			for resp in openai.Completion.create(model='text-davinci-003',
							prompt="Create a list of Titles to begin writing about with a" + Genre + " theme and a " + dropdown_menu + " tone.",
							max_tokens=1012, 
							temperature = slider,
							stream = True):
					report.append(resp.choices[0].text)
					result = "".join(report).strip()
					result = result.replace("\n", "")
					res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

			if Rewrite & selected2:
				speech = BytesIO()
				speech_ = gTTS(
					text=result, 
					lang='en', 
					slow=False
				)
				speech_.write_to_fp(speech)
				st.audio(speech)				
			st.download_button('Save Response', result,key="847*")		
	memory = []

Rewrite = st.button("Rewrite", help="Rewrite", key='996', use_container_width=False)

if Rewrite:
	report = []
	for resp in openai.Completion.create(model='text-davinci-003',
					prompt="Rewrite this, " + user_input + ", using a" + dropdown_menu + " tone:",
					max_tokens=1012, 
					temperature = slider,
					stream = True):
			report.append(resp.choices[0].text)
			result = "".join(report).strip()
			result = result.replace("\n", "")
			res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

	if Rewrite & selected2:
		speech = BytesIO()
		speech_ = gTTS(
			text=result, 
			lang='en', 
			slow=False
		)
		speech_.write_to_fp(speech)
		st.audio(speech)				
	st.download_button('Save Response', result,key="847*")


Summarize = st.button("Summarize", help="Summarize", key='994', use_container_width=False)
if Summarize:
	report = []
	for resp in openai.Completion.create(model='text-davinci-003',
					prompt="Summarize this, " + user_input + ", using a" + dropdown_menu + " tone:",
					max_tokens=1012, 
					temperature = slider,
					stream = True):
			report.append(resp.choices[0].text)
			result = "".join(report).strip()
			result = result.replace("\n", "")
			res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

	if Rewrite & selected2:
		speech = BytesIO()
		speech_ = gTTS(
			text=result, 
			lang='en', 
			slow=False
		)
		speech_.write_to_fp(speech)
		st.audio(speech)				
	st.download_button('Save Response', result,key="847*")
Brainstorm = st.button("Brainstorm", help="Summarize", key='992', use_container_width=False)
if Brainstorm:
	report = []
	for resp in openai.Completion.create(model='text-davinci-003',
					prompt="Brainstorm and create a list of 10-20 creative writing ideas.",
					max_tokens=1012, 
					temperature = slider,
					stream = True):
			report.append(resp.choices[0].text)
			result = "".join(report).strip()
			result = result.replace("\n", "")
			res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

	if Rewrite & selected2:
		speech = BytesIO()
		speech_ = gTTS(
			text=result, 
			lang='en', 
			slow=False
		)
		speech_.write_to_fp(speech)
		st.audio(speech)				
	st.download_button('Save Response', result,key="847*")		
Title = st.button("Create Title", help="Create Titles", key='990', use_container_width=False)
if Title:
	report = []
	for resp in openai.Completion.create(model='text-davinci-003',
					prompt="Create a list of Titles to begin writing about with a" + Genre + " theme and a " + dropdown_menu + " tone.",
					max_tokens=1012, 
					temperature = slider,
					stream = True):
			report.append(resp.choices[0].text)
			result = "".join(report).strip()
			result = result.replace("\n", "")
			res_box.markdown(f":blue[Bellaxtrix:  ]:green[*{result}*]")

	if Rewrite & selected2:
		speech = BytesIO()
		speech_ = gTTS(
			text=result, 
			lang='en', 
			slow=False
		)
		speech_.write_to_fp(speech)
		st.audio(speech)				
	st.download_button('Save Response', result,key="847*")		
memory = []

st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BBWeb App!&body=Please specify the issue you are facing with the app.'><strong>BlackBots</strong></a></center><hr>", unsafe_allow_html=True)

st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
