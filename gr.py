from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
import pandas as pd
import numpy as np
import matplotlib as mp
import time
import pprint
import streamlit as st

cl = Client()
cl.delay_range = [2, 6]
def login_user():

    cl = Client()
    session = cl.load_settings("session.json")

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")
      
st.header("IG BlackMarket")
USERNAME = st.text_input("Enter Username:")
PASSWORD = st.text_input("Enter Password:", type="password")
Keyy = st.text_input("Set API-Key:")
Go = st.button('Start')
if Go:
  try:cl.load_settings("session.json");
  except:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings("session.json")
  login_user()
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
      username_str = name
      hashtag_list = ["like", "follow", "follow", "chatgpt", "ai", "chatai"]
  
      for hashtag in hashtag_list:
          top_posts = cl.hashtag_medias_top(hashtag, find_value)
  
          for i in range(0, len(top_posts)):
              first_comment = top_posts[i].dict()
  
              post_id = first_comment['id']  
              post_code = first_comment['code']
              post_url = "https://instagram.com/reel/" + post_code
              st.write(post_url)
  
              media_id = cl.media_id(cl.media_pk_from_url(post_url))
              
              is_present = False
  
              post_id = media_id
  
              if  is_present == False:
                  st.write("New Post Found, Commenting..... \n")
                  try:
                      ai_comm = "Write a nice generic Instagram Photo comment pertaining to a pleasant picture and ask for whomever to checkout your instagram page which is " + username_str + "."
                      text = "Nice!"
                      comment = cl.media_comment(post_id, str(text))
                      st.write('Comment Left!')
                      time.sleep(200)
                  except Exception as error:
                      st.write(error)
  
              else:
                  print("Post Already Found \n")
      # Increase the time inorder to not get temporary ban
      st.write("New Posts in 5 Seconds....")
      time.sleep(60)
  
      
