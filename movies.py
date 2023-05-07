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

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

# link is the column with hyperlinks
df['link'] = df['link'].apply(make_clickable)
df = df.to_html(escape=False)
st.write(df, unsafe_allow_html=True)

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
with st.sidebar:
        cols = st.columns(2)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
