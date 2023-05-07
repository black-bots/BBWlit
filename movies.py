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
st.title("Let's create a table!")
for i in range(1, 10):
    cols = st.columns(4)
    cols[0].write(f'{i}')
    cols[1].write('Black Bots 1')
    cols[2].write(f'{i * i * i}')
    cols[3].write('Black Bots 3')
################################
