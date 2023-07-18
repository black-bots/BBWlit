from instagrapi import Client
import pandas as pd
import numpy as np
import matplotlib as mp
import time
import pprint
import openai
import prompt_toolkit
import streamlit as st

st.header("IG BlackMarket")
name = st.text_input("Enter Username:")
password = st.text_input("Enter Password:", type="password")
Keyy = st.text_input("Set API-Key:")
Go = st.button('Start')
if Go:
  cl = Client()
  cl.login(name, password)
  openai.api_key = Keyy
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
                      text = generate_response(ai_comm)
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
  
      
