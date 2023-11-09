import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import GridOptionsBuilder, AgGrid, JsCode
from st_aggrid.shared import ColumnsAutoSizeMode
import pandas as pd
import numpy as np
from PIL import Image
#STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true

image = Image.open('static/p1.png')
image1 = Image.open('static/p1.jpg')
st.image(image,use_column_width=True)
st.markdown("""---""")

def paginator(label, items, items_per_page=10, on_sidebar=False):
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

st.markdown("""
  <style>
    html {
	text-align: center;
	display: block;
	margin-left: auto;
	margin-right: auto;
    }

    .st-emotion-cache-1v0mbdj {
	text-align: center;
	display: block;
	margin-left: auto;
	margin-right: auto;    
    }
    .st-emotion-cache-16idsys.e1nzilvr5 {
      font-weight: 900;
      color: orange;
      }
    .st-emotion-cache-16idsys p {
      font-size: 16px;
      }
    p {
      font-family: bariol;
      font-size: 16px;
      }
  </style>
""", unsafe_allow_html=True)
ft = """
<style>
	a:link , a:visited{
	color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
	background-color: transparent;
	text-decoration: none;
	}
	
	a:hover,  a:active {
	color: #0283C3; /* theme's primary color*/
	background-color: transparent;
	text-decoration: underline;
	}
	
	#page-container {
	  position: relative;
	  min-height: 10vh;
	}
	
	footer{
	    visibility:hidden;
	}
	
	.footer {
  	position:fixed;
	index: 9999;
   	left: 0;
	bottom: 0;
	width: 100%;
	background-color: transparent;
	color: #808080; /* theme's text color hex code at 50 percent brightness*/
	text-align: left;
	}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'> Made by <a style='display: inline; text-align: left;' href="https://blackbots.net/" target="_blank">BlackBots.net</a><img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
with st.expander("Pierre Polie",expanded=False):
	st.write(f"""
	:green[Engagement & Fashion Jewelry from Pierre Polie]
 
	:blue[What is the perfect way to dress up any outfit or add your own flare? Accessorizing with jewelry, of course! From sparkling diamond necklaces and fashionable layered bracelets to statement earrings to sophisticated but trendy stackable rings,Pierre Polie has the perfect jewelry piece to accentuate your wardrobe, your lifestyle and your budget.] 
 
	:blue[Who says men can't dress up their wardrobe too?! Find sophisticated and handsome jewelry for men such as necklaces and chains.Whether there's a major event or you're looking for something just because, our selection of men's jewelry and gift ideas has everything you need and more. Are you overwhelmed by the idea of finding an engagement ring and proposing? Let Pierre Polie guide you in the right direction with our seemingly endless possibilities of engagement ring styles.] 
	
	:blue[No matter if you're celebrating a first anniversary or a 25 year anniversary, a wedding anniversary gift is always cherished and appreciated. Let Pierre Polie be your guide in finding the perfect anniversary gift for him or for her today. Show your wedding party how much they mean to you with a beautiful bridesmaid gift, groomsman gift, or even flower girl gift from our wedding party gift selection at Pierre Polie.]
	""")

st.markdown("""---""")

st.write("Todays Featured Piece")
st.image('https://static.wixstatic.com/media/0dfae7_0827377152164dffb725932fa01092c9~mv2.jpg/v1/fill/w_1000,h_1000/ring%2020%20-%202.jpg', width=600)
components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>

<h2>Automatic Slideshow</h2>
<p>Change image every 2 seconds:</p>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920" style="width:100%">
  <div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920" style="width:100%">
  <div class="text">Caption Three</div>
</div>

</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
</script>

</body>
</html> 

    """,
    height=600,
)

st.markdown("""---""")

st.header("Featured Sets")
col1, col2, col3, col4= st.columns(4)

with col1:
   st.write("Set1")
   st.text("RandomName")
   st.image('https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg', width=175)
   st.write("[View More](https://link-center.net/674202/free-mario-bros-movie)")
   

with col2:
   st.write("Set2")
   st.text("RandomName")
   st.image('https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg', width=175)
   st.write("[View More](https://link-center.net/674202/free-mario-bros-movie)")


with col3:
   st.write("Set3")
   st.text("RandomName")
   st.image('https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg', width=175)
   st.write("[View More](https://link-center.net/674202/free-mario-bros-movie)")

    
with col4:
   st.write("Set4")
   st.text("RandomName")
   st.image('https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg', width=175)
   st.write("[View More](https://link-center.net/674202/free-mario-bros-movie)")


Rings = [
	image1,
	'https://static.wixstatic.com/media/0dfae7_50700c2ac4a1434c9149ecd7d16f2f73~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_7af924f0a89d4c28b11d36f51a3df542~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_0f27f377533746b580637d433e7326c4~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_13f6f0f1de97447db6c8b31809dfd4d6~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_67c2f9eb5c61465ca54def74b745e1f2~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_f545a5f877d64bf3afeb4e28dcb1394c~mv2.jpg',
	'https://static.wixstatic.com/media/0dfae7_0827377152164dffb725932fa01092c9~mv2.jpg/v1/fill/w_1000,h_1000/ring%2020%20-%202.jpg'
]
image_iterator = paginator("Rings", Rings)
indices_on_page, images_on_page = map(list, zip(*image_iterator))
st.image(images_on_page, width=300, caption=indices_on_page)

expd2 = st.expander("View More Pieces", expanded=False)

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

with st.sidebar:
    st.subheader("MENU")
    st.markdown("""---""")

    st.write('[Rings]()')
    st.write('[Necklaces]()')
    st.write('[Bracelets]()')
    st.markdown("""---""")
