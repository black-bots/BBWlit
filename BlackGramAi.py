import streamlit as st
import instaloader

st.header("Who's not following back?")
name = st.text_input("Enter user name")
password = st.text_input("Enter password", type="password")
L = instaloader.Instaloader()

Go = st.button('Check for Unfollowers')
if Go:
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
