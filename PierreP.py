import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
#STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true

image = Image.open('static/p1.png')
st.image(image,use_column_width=True)

st.markdown('-:green[Supremely Refined]')
featured = st.expander("Todays Featured Piece", expanded=True)
with featured:
	components.html("""<iframe src="https://static.wixstatic.com/media/0dfae7_8ebd2fd403514153a649d4fc899838e9~mv2.jpg" width="300" height="300" />""",width=301,height=301)


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
   st.write("🎥👉 [Watch Movie](https://link-center.net/674202/free-mario-bros-movie)")
   

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
st.write(f"""
:blue[1: ]Click on the link (next to 🎥👉)

:blue[2: ]Click on “Free Access” on the Linkvertise page that opens up (You DO NOT need to purchase Premium)

:blue[3: ]Click on “Discover articles” under ‘Complete the follow steps’ – It will open a popup titled “Interesting articles from the web!” 

:blue[3.1: ] Click the black X on the right hand side. – Might have to wait 10 seconds. – Then click “Continue”

:red[For Mobile:] IF “Download an App” Step appears – Click on this and then click “Download” so the App store opens but DO NOT download the game. Take 60 seconds to chill or roll up, then return to your browser, to the page and the small window that had the “Download” button should be gone and you can continue to the movie.
""")

col1, col2, col3, col4= st.columns(4)

with col1:
   st.write("Ant-Man and the Wasp: Quantumania")
   st.text("Trailer")
   st.video('https://youtu.be/ZlNFpri-Y40')
   st.write("🎥👉 [Watch Movie](https://link-target.net/674202/free-new-movies-2023)")
   

with col2:
   st.write("Shazam! Fury of the Gods")
   st.text("Trailer")
   st.video('https://youtu.be/Zi88i4CpHe4')
   st.write("🎥👉 [Watch Movie](https://link-center.net/674202/free-mario-bros-movie)")


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

expd2 = st.expander("View More Movies", expanded=False)
with expd2:
    col1, col2, col3, col4= st.columns(4)

    with col1:
       st.write(":red[Server Undergoing Maintenance]")
    with col2:
       st.write(":red[Server Undergoing Maintenance]")
    with col3:
       st.write(":red[Server Undergoing Maintenance]")
    with col4:
       st.write(":red[Server Undergoing Maintenance]")

##############################################

with st.sidebar:
    st.subheader("NOW SHOWING")
    st.write('[John Wick: Chapter 4 (2023)](https://direct-link.net/674202/free-evil-dead-rise-movie)')
    st.write('[The Super Mario Bros. Movie (2023)](https://link-center.net/674202/free-mario-bros-movie)')
    st.write('[Evil Dead Rise (2023)](https://direct-link.net/674202/free-evil-dead-rise-movie)')
    st.write('[Scream VI (2023)](https://link-hub.net/674202/free-scream-iv-movie)')
    st.write('[Ant-Man and the Wasp: Quantumania](https://link-target.net/674202/free-new-movies-2023)')
    st.write("[Shazam! Fury of the Gods](https://link-target.net/674202/free-new-movies-2023)")
    st.write('[Dungeons & Dragons: Honor Among Thieves (2023)](https://link-target.net/674202/free-new-movies-2023)')
    st.write("[The Pope's Exorcist (2023)](https://link-target.net/674202/free-new-movies-2023)")
    st.write('[Guardians of the Galaxy Vol. 3 (2023)](https://link-target.net/674202/free-new-movies-2023)')
    st.write("[Are You There God? It's Me, Margaret. (2023)]()")
    st.write('[Sisu (2023)]()')
             
