import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('static/1.png')
def my_widget(key):
    st.subheader('Hello there!')
    return st.button("Click me " + key)

# This works in the main area
clicked = my_widget("first")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")
    
#############################
st.title("Movies List")
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    for i in range(1, 5):
        cols = st.columns(4)
        cols[0].write('the Super Mario Movie')
        cols[1].write('Evil Dead Rise')
        cols[2].write('Scream VI')
        cols[3].write('John Wick: Chapter 4')
################################
