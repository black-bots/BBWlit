import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
#STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true

image = Image.open('static/p1.png')
image1 = Image.open('static/p1.jpg')
st.image(image,use_column_width=True)

st.markdown('-:green[Supremely Refined]')
featured = st.expander("Todays Featured Piece", expanded=True)
def paginator(label, items, items_per_page=1, on_sidebar=False):
    if on_sidebar:
        location = st.sidebar.empty()
    else:
        location = st.empty()

    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // items_per_page + 1
    page_format_func = lambda i: "Page %s" % i
    page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)
    min_index = page_number * items_per_page
    max_index = min_index + items_per_page
    import itertools
    return itertools.islice(enumerate(items), min_index, max_index)


with featured:
	features = [
	    image1,
	    'https://static.wixstatic.com/media/0dfae7_0827377152164dffb725932fa01092c9~mv2.jpg/v1/fill/w_1000,h_1000/ring%2020%20-%202.jpg'
	]
	image_iterator = paginator("Diamond Saucer", features)
	indices_on_page, images_on_page = map(list, zip(*image_iterator))
	st.image(images_on_page, width=300, caption=indices_on_page)

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

Page1 = [
	'https://static.wixstatic.com/media/0dfae7_5ba237552d6746c1aa8459751237a8cb~mv2.jpg/v1/fill/w_274,h_274,al_c,q_80,usm_0.66_1.00_0.01/0dfae7_5ba237552d6746c1aa8459751237a8cb~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_50700c2ac4a1434c9149ecd7d16f2f73~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_7af924f0a89d4c28b11d36f51a3df542~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_0f27f377533746b580637d433e7326c4~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_67c2f9eb5c61465ca54def74b745e1f2~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_f545a5f877d64bf3afeb4e28dcb1394c~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_0827377152164dffb725932fa01092c9~mv2.jpg/v1/fill/w_1000,h_1000/ring%2020%20-%202.jpg'
]
image_iterator = paginator("Rings", Page1)
indices_on_page, images_on_page = map(list, zip(*image_iterator))
st.image(images_on_page, width=300, caption=indices_on_page)

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
             
