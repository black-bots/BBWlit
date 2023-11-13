import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from PIL import Image
import stwextra
import requests
import json
import time
import urllib.request
import speech_recognition as sr
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from wit import Wit
import webbrowser

#AssemblyAI
api_key =  "ef7ed5978b1b48a38582799dce314a7a"
icob = Image.open('-.ico')
_image = Image.open('--.png')
mp3 = "1.mp3"
wav = "2.wav"

st.set_page_config(
    page_title="ScribieTrans WEB",
    initial_sidebar_state="expanded",
    page_icon=icob,
    layout="centered",
    menu_items={
        'Get Help': 'https://github.com/xtekky/gpt4free/blob/main/README.md',
        'Report a bug': "https://github.com/xtekky/gpt4free/issues",
        'About': "### gptfree GUI",
    },
)

def Conv():
    st.caption("(Trying)")
    urllib.request.urlretrieve(urlnk, "1.mp3")
    mp3 = "1.mp3"
    wav = "2.wav"
    st.markdown("••• Converting file •••")
    sound = AudioSegment.from_mp3(mp3)
    sound.export(wav, format="wav")
    print("\n")
    st.caption("(Complete)")
    st.markdown("••• File converted •••")
    time.sleep(4)
    Transit()

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def upload_file(api_token, path):

    st.caption("(Checking)")
    st.markdown(f"••• File: {path} •••")
    headers = {'authorization': api_token}
    
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(path))

    if response.status_code == 200:
        return response.json()["upload_url"]

    else:
        st.caption(f"Error: {response.status_code}")
        st.markdown(f"••• - {response.text} •••")
        return None

def create_transcript(api_token, audio_url):

    st.caption("(Running)")
    st.markdown("••• Transcribing audio... This might take a moment. •••")
    url = "https://api.assemblyai.com/v2/transcript"

    headers = {
        "authorization": api_token,
        "content-type": "application/json"
    }

    data = {
        "audio_url": audio_url
    }

    response = requests.post(url, json=data, headers=headers)

    transcript_id = response.json()['id']

    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()

        if transcription_result['status'] == 'completed':
            st.caption("(Complete)")
            st.markdown("••• Transcription Complete •••")
            break

        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        else:
            time.sleep(3)

    return transcription_result

def Transit():
    your_api_token = api_key

    filename = wav

    upload_url = upload_file(your_api_token, filename)

    transcript = create_transcript(your_api_token, upload_url)
    st.caption("Transcription :")
    st.markdown(transcript)
    print(transcript, file=open('Transcribed.txt', 'w'))
    webbrowser.open("Transcribed.txt")


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
                background: #3DD56D;
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
            footer {visibility: hidden;}
        </style>
    """,
    unsafe_allow_html=True
    )


st.header('ScribieTrans WEB')

urlnk = st.text_input('Enter media url for transcription:', placeholder='www.websitename.com/audio.mp3')
transb = st.button("🤖 Transcribe")
if transb:
        Conv()

st.image(_image,use_column_width='auto')
