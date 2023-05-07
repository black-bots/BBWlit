import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('static/ori_3748732_mkqg8a0irpybxk8xtejrqetwi9j3f3011wq3dyi1_online-cinema-banner-vector-realistic-computer-monitor-movie-brochure-design-template-banner-for-movie-premiere-show-marketing-luxury-poster-illustration.jpg')
st.image(image,use_column_width=True)

def my_widget(key):
    st.subheader('Hello there! tavos')
    return st.button("Click me " + key)
def my_widget2(key):
    st.subheader('gooodbyeees')
    return st.button("Click me " + key)

#############################
st.title("Movies List")
my_expander = st.expander("Expand", expanded=True)
with my_expander:
        cols = st.columns(4)
        cols[0].write('the Super Mario Movie',my_widget("Click"))
        cols[1].write('Evil Dead Rise')
        cols[2].write('Scream VI')
        cols[3].write('John Wick: Chapter 4')
# This works in the main area
clicked = my_widget("first")
################################
with st.sidebar:
    clicked = my_widget("third")
