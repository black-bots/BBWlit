import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

image = Image.open('static/ori_3748732_mkqg8a0irpybxk8xtejrqetwi9j3f3011wq3dyi1_online-cinema-banner-vector-realistic-computer-monitor-movie-brochure-design-template-banner-for-movie-premiere-show-marketing-luxury-poster-illustration.jpg')
st.image(image,use_column_width=True)

def my_widget2(key):
    st.subheader('Watch Now')
    return st.button("Click me " + key)

#############################
st.subheader("Movies List")

expd = st.expander("Expand", expanded=False)
with expd:
        cols = st.columns(6)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
        cols[2].write('Scream VI')
        cols[3].write('John Wick: Chapter 4')
        cols[4].write(image)
        cols[5].write(my_widget2('-'))
################################
st.subheader("Movie List")
expd2 = st.expander("Expand", expanded=False)
with expd2:
    data = pd.read_csv('https://gist.githubusercontent.com/KonuTech/5ef61b6754b03f00c0baf393bbe66691/raw/c7924c7906f290a53714c3d8bdaa04cbd0ebcc05/movies_data.csv')
    data

    column_names = list(data.columns)
    data[0].write('the Super Mario Movie')
    select = st.selectbox("Choose your movie", column_names)

    st.write("Your selection",select)
##############################################
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image(image)

with col2:
   st.header("A dog")
   st.image(image)

with col3:
   st.header("An owl")
   st.image(image)

with st.sidebar:
        cols = st.columns(2)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
