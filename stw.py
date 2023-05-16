import requests
import json
import time
import urllib.request
import speech_recognition as sr
import os
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from wit import Wit
import webbrowser

#AssemblyAI
api_key =  ""


if input("\n••• Use url?(yes or no): ") == "yes":
    url = input("Enter .mp3 URL: ")
    urllib.request.urlretrieve(url, "1.mp3")
else:
    pass

def Conv():
    print("\n••• (Trying)Converting file •••")
    sound = AudioSegment.from_mp3(mp3)
    sound.export(wav, format="wav")
    print("\n••• (Complete)File converted •••")
    time.sleep(4)

mp3 = "1.mp3"
wav = "2.wav"
Conv()


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def upload_file(api_token, path):

    print(f"\n••• (Checking)File: {path} •••")
    headers = {'authorization': api_token}
    
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(path))

    if response.status_code == 200:
        return response.json()["upload_url"]

    else:
        print(f"\n••• Error: {response.status_code} - {response.text} •••")
        return None

def create_transcript(api_token, audio_url):

    print("\n••• (Running)Transcribing audio... This might take a moment. •••")

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
            print("\n••• (Complete)Transcription Complete •••")

            break

        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        else:
            time.sleep(3)

    return transcription_result

your_api_token = api_key

filename = wav

upload_url = upload_file(your_api_token, filename)

transcript = create_transcript(your_api_token, upload_url)
print(transcript, file=open('Transcribed.txt', 'w'))
webbrowser.open("Transcribed.txt")
