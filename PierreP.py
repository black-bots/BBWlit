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

with featured:

	def paginator(label, items, items_per_page=10, on_sidebar=True):
	    """Lets the user paginate a set of items.
	    Parameters
	    ----------
	    label : str
	        The label to display over the pagination widget.
	    items : Iterator[Any]
	        The items to display in the paginator.
	    items_per_page: int
	        The number of items to display per page.
	    on_sidebar: bool
	        Whether to display the paginator widget on the sidebar.
	        
	    Returns
	    -------
	    Iterator[Tuple[int, Any]]
	        An iterator over *only the items on that page*, including
	        the item's index.
	    Example
	    -------
	    This shows how to display a few pages of fruit.
	    >>> fruit_list = [
	    ...     'Kiwifruit', 'Honeydew', 'Cherry', 'Honeyberry', 'Pear',
	    ...     'Apple', 'Nectarine', 'Soursop', 'Pineapple', 'Satsuma',
	    ...     'Fig', 'Huckleberry', 'Coconut', 'Plantain', 'Jujube',
	    ...     'Guava', 'Clementine', 'Grape', 'Tayberry', 'Salak',
	    ...     'Raspberry', 'Loquat', 'Nance', 'Peach', 'Akee'
	    ... ]
	    ...
	    ... for i, fruit in paginator("Select a fruit page", fruit_list):
	    ...     st.write('%s. **%s**' % (i, fruit))
	    """
	
	    # Figure out where to display the paginator
	    if on_sidebar:
	        location = st.sidebar.empty()
	    else:
	        location = st.empty()
	
	    # Display a pagination selectbox in the specified location.
	    items = list(items)
	    n_pages = len(items)
	    n_pages = (len(items) - 1) // items_per_page + 1
	    page_format_func = lambda i: "Page %s" % i
	    page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)
	
	    # Iterate over the items in the page to let the user display them.
	    min_index = page_number * items_per_page
	    max_index = min_index + items_per_page
	    import itertools
	    return itertools.islice(enumerate(items), min_index, max_index)
	
	def demonstrate_paginator():
	    fruit_list = [
	        'Kiwifruit', 'Honeydew', 'Cherry', 'Honeyberry', 'Pear',
	        'Apple', 'Nectarine', 'Soursop', 'Pineapple', 'Satsuma',
	        'Fig', 'Huckleberry', 'Coconut', 'Plantain', 'Jujube',
	        'Guava', 'Clementine', 'Grape', 'Tayberry', 'Salak',
	        'Raspberry', 'Loquat', 'Nance', 'Peach', 'Akee'
	    ]
	    for i, fruit in paginator("Select a fruit page", fruit_list):
	        st.write('%s. **%s**' % (i, fruit))
	
	
	#if __name__ == '__main__':
	#    demonstrate_paginator()	
	sunset_imgs = [
	    'static/p1.jpg',
	    'https://static.wixstatic.com/media/0dfae7_8ebd2fd403514153a649d4fc899838e9~mv2.jpg',
	    'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
	    'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
	    'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
	    'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
	    'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
	    'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
	    'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
	    'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
	    'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
	    'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
	    'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
	    'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
	    'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
	]
	image_iterator = demonstrate_paginator("Select a sunset page", sunset_imgs)
	indices_on_page, images_on_page = map(list, zip(*image_iterator))
	st.image(images_on_page, width=100, caption=indices_on_page)
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
             
