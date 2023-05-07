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
st.title("Movies List")

my_expander = st.expander("Expand", expanded=True)
with my_expander:
        cols = st.columns(6)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
        cols[2].write('Scream VI')
        cols[3].write('John Wick: Chapter 4')
        cols[4].write(image)
        cols[5].write(my_widget2('-'))
################################
st.title("Pandas Dataframe selection")

data = pd.read_csv('top_100_movies.csv.html')
data

column_names = list(data.columns)

select = st.selectbox("Choose your movie", column_names)

st.write("Your selection",select)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.hist(select)

st.write(fig)

with st.sidebar:
        cols = st.columns(2)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
