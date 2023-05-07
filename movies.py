import streamlit as st
import pandas as pd
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
    cols[1].write(f'{i * i}')
    cols[2].write(f'{i * i * i}')
    cols[3].write('x' * i)
################################
col1, col2 = st.columns(2)

original = Image.open(image)
col1.header("Original")
col1.image(original, use_column_width=True)

grayscale = original.convert('LA')
col2.header("Grayscale")
col2.image(grayscale, use_column_width=True)
