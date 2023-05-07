import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

image = Image.open('static/ori_3748732_mkqg8a0irpybxk8xtejrqetwi9j3f3011wq3dyi1_online-cinema-banner-vector-realistic-computer-monitor-movie-brochure-design-template-banner-for-movie-premiere-show-marketing-luxury-poster-illustration.jpg')
st.image(image,use_column_width=True)

def my_widget2(key):
    st.subheader('Watch Now')
    return st.button("Click me " + key)

################################
st.header("Featured Movies")
col1, col2, col3, col4= st.columns(4)

with col1:
   st.write("the Super Mario Bros")
   st.text("Trailer")
   st.video('https://youtu.be/TnGl01FkMMo')
   st.write("🎥👉 [Watch Movi](https://link-center.net/674202/free-mario-bros-movie)")
   

with col2:
   st.write("Evil Dead")
   st.text("Trailer")
   st.video('https://youtu.be/0lmBDnliqKs')
   st.write("🎥👉 [Watch Movie](https://direct-link.net/674202/free-evil-dead-rise-movie)")


with col3:
   st.write("Scream VI")
   st.text("Trailer")
   st.video('https://youtu.be/1Ie2qmAOc6Q')
   st.write("🎥👉 [Watch Movie](https://link-hub.net/674202/free-scream-iv-movie)")

    
with col4:
   st.write("John Wick: Chapter 4")
   st.text("Trailer")
   st.video('https://youtu.be/qEVUtrk8_B4')
   st.write("🎥👉 [Watch Movie](https://direct-link.net/674202/free-john-wick-chapter-4)")

st.header("How to Watch Movies for FREE")
st.write("""
Click on the link (next to 🎥👉)

Click on “Free Access” on the Linkvertise page that opens up (You DO NOT need to purchase Premium)

Click on “Discover articles” under ‘Complete the follow steps’ – It will open a popup titled “Interesting articles from the web!” 

– Click the black X on the right hand side. – Might have to wait 10 seconds. – Then click “Continue”

For Mobile: IF “Download an App” Step appears – Click on this and then click “Download” so the App store opens but DO NOT download the game. Take 60 seconds to chill or roll up, then return to your browser, to the page and the small window that had the “Download” button should be gone and you can continue to the movie.
""")

expd2 = st.expander("View More", expanded=False)
with expd2:
    col1, col2, col3, col4= st.columns(4)

    with col1:
       st.write("the Super Mario Bros")
       st.text("Trailer")
       st.video('https://youtu.be/TnGl01FkMMo')
       st.write("🎥👉 [Watch Movi](https://link-center.net/674202/free-mario-bros-movie)")


    with col2:
       st.write("Evil Dead")
       st.text("Trailer")
       st.video('https://youtu.be/0lmBDnliqKs')
       st.write("🎥👉 [Watch Movie](https://direct-link.net/674202/free-evil-dead-rise-movie)")


    with col3:
       st.write("Scream VI")
       st.text("Trailer")
       st.video('https://youtu.be/1Ie2qmAOc6Q')
       st.write("🎥👉 [Watch Movie](https://link-hub.net/674202/free-scream-iv-movie)")


    with col4:
       st.write("John Wick: Chapter 4")
       st.text("Trailer")
       st.video('https://youtu.be/qEVUtrk8_B4')
       st.write("🎥👉 [Watch Movie](https://direct-link.net/674202/free-john-wick-chapter-4)")

##############################################

with st.sidebar:
    st.subheader("NOW SHOWING")
    cols = st.columns(4)
    cols[0].write('the Super Mario Movie')
    cols[1].write('Evil Dead Rise')
    cols[2].write('Scream VI')
    cols[3].write('John Wick: Chapter 4')

