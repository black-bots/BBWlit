from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
import pandas as pd
import random
import numpy as np
import matplotlib as mp
import time
import pprint
import streamlit as st
from PIL import Image


bottom_image = Image.open('static/1.png')
main_image = Image.open('static/-.ico')
top_image = Image.open('static/4.png')
_image = Image.open('static/3.png')

st.image(bottom_image,use_column_width='auto')

USERNAME = st.text_input("Enter Username:")
PASSWORD = st.text_input("Enter Password:", type="password")
find_value = 10

st.markdown(
    '<style>'
    '<br><hr><center>'
    '.embeddedAppMetaInfoBar_container__LZA_B{visibility:hidden;}'
    'button:hover {'
    'background-color: orange;'
    'transition: all 0.3s ease-in-out;'
    '}'
    '.st-ck:hover {'
    'color: #3DD56D;'
    '}'
    '.st-c6 {'
    'color: #FFBD45;'
    '}'
    '.st-mh:hover {'
    'background-color: grey;'
    'color: gold;'
    'border: 2px solid #FFBD45;'
    'box-shadow: 0 0 10px #FFBD45;'
    'transition: all 0.3s ease-in-out;'
    'border-color: #FFBD45;'
    'cursor: pointer;'
    '}'

    'img {'
    'width:50%;'
    '}'
    '.css-1v0mbdj{'
    'width:578px;'
    'vertical-align: middle;'
    'horizontal-align: middle;'
    'max-width: 300px;'
    'margin: auto;'
    '}'
    '.css-yhwc6k{'
    'text-align: center;'
    '}'
    '#audio{autoplay:true;}'
    '#MainMenu{visibility: hidden;}'
    'footer{visibility: hidden;}'
    '.css-14xtw13 e8zbici0{visibility: hidden;}'
    '</style>',
    unsafe_allow_html=True
)


with st.sidebar:
	st.info('SETTINGS', icon="ℹ️")
	
	hashes = st.selectbox(
		'Tag',
		("all", "anime", "art", "beauty", "blessed", "blog", "blogger", "cute", "exercise", "fashion", "fitness", "follow", "followme", 
		 "foodie", "friends", "fun", "girl", "goals", "happy", "itod", "instagood", "instadaily", "life", "love", "me", 
		 "manga", "motivation", "nature", "ootd", "photooftheday", "picoftheday", "potd", "selfie", "smile", "style", "summer", 
		 "sun", "swag", "tbt", "throwback", "tiktok", "travel", "trend", "trending", "vacation", "vibes", "wedding", "weekend", 
		 "workout", "x", "yolo", "yougotthis", "youtube", "yummy", "ootd", "inspiration", "photography"
		),help="Select a Tag to set the botting demographic")

	top_select = st.selectbox('Posts',('Top Posts','Recent Posts'),help="Choose which Posts to interact with")

	dropdown_menu = st.selectbox(
		'Direct Traffic',
		('to Profile', 'to Inbox', 'to Bio-Link'),help="Select where bot will direct people to go with it's comment")

	slider_value = st.slider(':orange[Wait Time]', 1, 30, 60, step=1,help="Minutes to wait in between likes")

	if dropdown_menu == 'to Profile':
	    # Comments directing the reader to check out the commenter's profile.
	    comments = [
	        "Hey there! I'd love it if you checked out my profile! 😊",
	        "If you have a moment, feel free to swing by my profile! 🌟",
	        "Curious about what I post? You can find out on my profile! 👀",
	        "Want to see more content like this? Check out my profile! 😄",
	        "Thanks for stopping by! If you're interested, my profile is just a click away! 💫",
	        "If you enjoy my comments, you might like what's on my profile! 📸",
	        "Hey! If you want to see more, my profile is where it's at! 🚀",
	        "Feel free to explore my profile if you're interested! 🌈",
	        "Thanks for your support! If you want to see more, head over to my profile! 🙌"
	    ]
	elif dropdown_menu == 'to Inbox':
	    # Comments directing the reader to check the commenter's inbox.
	    comments = [
	        "If you'd like to chat further, feel free to slide into my DMs! 💌",
	        "Got something to say? Shoot me a message in my inbox! 📩",
	        "If you have any questions or just want to chat, my inbox is open! 😊",
	        "Feel free to drop me a message in my inbox if you'd like to connect! 👋",
	        "If you want to reach out for any reason, my inbox is always open! 📬",
	        "I love connecting with new people! Don't hesitate to send me a message! 😄",
	        "Feel free to reach out if you ever want to chat! My inbox is waiting! 💬",
	        "If you have any questions or just want to say hi, my inbox is the place to do it! 👋",
	        "If you ever want to connect one-on-one, my inbox is open for you! 🌟"
	    ]
	elif dropdown_menu == 'to Bio-Link':
	    # Comments directing the reader to visit the commenter's bio or link with enticing language.
	    comments = [
	        "Curious about what's in my bio? Click the link to find out more! 🔗",
	        "I've got some cool stuff in my bio! Click the link to explore! 🌟",
	        "Want to learn more about me? Check out my bio link! 😊",
	        "Discover valuable resources and exciting updates in my bio link! Click to explore! 👀",
	        "There's a surprise waiting for you in my bio link! Click to uncover it! 😄",
	        "My bio link holds secrets to success and inspiration! Click to reveal them! 🚀",
	        "Unlock exclusive content and special offers in my bio link! Click to access! 🌈",
	        "Find solutions to your problems and inspiration for your journey in my bio link! ❤️",
	        "Your next adventure begins with a click on my bio link! Explore it now! 😊"
	    ]

	hashtag_list = hashes

Go = st.button('Start')
if Go:

	slider = slider_value
	
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

	try:
		cl.load_settings("session.json")
	except:
		cl.login(USERNAME, PASSWORD)
		cl.dump_settings("session.json")
	login_user()
	
	while True:
		username_str = USERNAME
		try:
			if top_select == 'Top Posts':
				top_selected = cl.hashtag_medias_top(hashtag, amount=find_value)
			elif top_select == 'Recent Posts':
				top_selected = cl.hashtag_medias_recent(hashtag, amount=find_value)
			hashtag = hashtag_list
			top_posts = top_selected
			st.write("Tag: " + hashtag)
			for i in range(0, len(top_posts)):
				first_comment = top_posts[i].dict()
			post_id = first_comment['id']  
			post_code = first_comment['code']
			post_url = "https://instagram.com/reel/" + post_code			
			media_id = cl.media_id(cl.media_pk_from_url(post_url))
			
			is_present = False
			
			post_id = media_id
			
			if  is_present == False:
				st.write("Post Found, Commenting..... \n")
				try:
					comments = random.choice(comments)
					text = comments
					comment = cl.media_comment(post_id, str(text))
					st.write('Comment: ' + text)
					st.write('Post: ' + post_url)
				except Exception as error:
					st.write(error)
			else:
				print("Post Already Found \n")
			# Increase the time inorder to not get temporary ban
			st.write(f"New Posts in {slider} minutes....")
			time.sleep(slider * 60)
		except Exception as e:
			print("Error occurred:", e)
			import traceback
			traceback.print_exc()
			
st.markdown("<br><hr><center>© Cloud Bots™ BlackBots. All rights reserved. by <a href='mailto:admin@blackbots.net?subject=BlackGram!&body=To whom it may concern: '><strong>BlackBots.net</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
