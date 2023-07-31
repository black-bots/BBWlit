import streamlit as st
import instaloader

from instagrapi import Client
import pandas as pd
import numpy as np
import matplotlib as mp
import time
import pprint
import openai
import prompt_toolkit

st.header("BlackGram")
name = st.text_input("Enter user name")
password = st.text_input("Enter password", type="password")
APIkey = st.text_input("Enter API-Key", type="password")

Start = st.button('Run BlackGram')
if Start:
    cl = Client()
    cl.login(str(name), str(password))
    openai.api_key = APIkey
    find_value = 20
    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=3600,
            n=1,
            stop=None,
            temperature=1,
        )
        message = response.choices[0].text.strip()
        return message
    while True:
        username_str = 'erikrai.tech'
        # List of Hashtags To Fetch
        hashtag_list = ["like", "follow", "follow", "chatgpt", "ai", "chatai"]
    
        for hashtag in hashtag_list:
            # Finding Top Hashtags Based on "find_value"
            top_posts = cl.hashtag_medias_top(hashtag, find_value)
    
            for i in range(0, len(top_posts)):
                first_comment = top_posts[i].dict()
    
                post_id = first_comment['id']
                #pprint.pprint(post_id)
    
                post_code = first_comment['code']
                #pprint.pprint(post_code)
                post_url = "https://instagram.com/reel/" + post_code
                print(post_url)
    
                media_id = cl.media_id(cl.media_pk_from_url(post_url))
                
                is_present = False
    
                post_id = media_id
    
                if  is_present == False:
                    st.write("New Post Found, Commenting.....")
                    try:
                        ai_comm = "Write a nice generic Instagram Photo comment and ask for whomever to checkout @BlackBots.tech for useful Ai Tools, Software & Electronics."
                        text = generate_response(ai_comm)
                        comment = cl.media_comment(post_id, str(text))
                        print(f'Commentd:\n{text}')
                        time.sleep(5)
                    except Exception as error:
                        print(error)
    
                else:
                    print("Post Already Found \nSearching..\n")
        st.write("New Posts in 8 Seconds....")
        time.sleep(8)


st.header("Who's not following back?")
Go = st.button('Check for Unfollowers')
if Go:
    L = instaloader.Instaloader()
    # Login or load session
    L.login(name, password)        # (login)

    profile = instaloader.Profile.from_username(L.context, name)
    main_followers = profile.followers

    follower_list = []
    for person in profile.get_followers():
      user_id = person.userid
      follower_list.append(person.username)

    main_followees = profile.followees
    followee_list = []
    for person in profile.get_followees():
      user_id = person.userid
      followee_list.append(person.username)

    req = []
    for element in followee_list:
      if element not in follower_list:
        req.append(element)

    st.write(sorted(req))
