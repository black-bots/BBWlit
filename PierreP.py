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

products = {
    "No.": [1, 2, 3],
    "Name": [' Chair', ' Cabinet', ' Table'],
    "Price": [4, 12, 10],
    "Stocks": [100, 50, 60],
    "Details": [
        "https://i.imgur.com/fH2LHvo.png",
        "https://i.imgur.com/bvHZX5j.png",
        "https://i.imgur.com/D7xDwT9.png"
    ]
}

df = pd.DataFrame(products)

ob = GridOptionsBuilder.from_dataframe(df)

# 1. Add an image next to the value under the Name column.
#    Also add a link on the label.
image_cr = JsCode("""
    function(params) {
        var element = document.createElement("span");

        var imageElement = document.createElement("img");
        var anchorElement = document.createElement("a");

        // Update the image element. Use the value from Details column.
        imageElement.src = params.data.Details;
        imageElement.width="80";
        imageElement.height="80";
        element.appendChild(imageElement);

        // Add a link to the Name value. The link is from the Details column.
        anchorElement.href = params.data.Details;
        anchorElement.target = "_blank";
        anchorElement.innerHTML = params.value;
        element.appendChild(anchorElement);

        return element;
    }""")
ob.configure_column('Name', cellRenderer=image_cr)

# 2. Configure the column Details. Add a link to inner value.
image_url = JsCode("""
    function(params) {
        return `<a href=${params.value} target="_blank">${params.value}</a>`
    }""")
ob.configure_column("Details", cellRenderer=image_url)

# 2.1. Style the cell, if stocks is below 60, increase font-size
#      and color it red - as a warning to supply department.
low_supply = JsCode("""
    function(params) {
        if (params.value < 60) {
            return {
                'color': 'red',
                'font-size': '20px'
            };
        }
    }""")
ob.configure_column("Stocks", cellStyle=low_supply)

# 3. Update selection.
ob.configure_selection(selection_mode="multiple", use_checkbox=True)

# 4. Update row height, to make the image look clearer.
ob.configure_grid_options(rowHeight=100)

# 5. Hide the Details column. The product name has a link already.
ob.configure_column("Details", hide=True)

# 6. Build the options.
grid_options = ob.build()

st.markdown('#### Streamlit-AgGrid')

# 7. Add custom css to center the values, as we adjusted the row height in step 4.
grid_return = AgGrid(
    df,
    grid_options,
    allow_unsafe_jscode=True,
    enable_enterprise_modules=False,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
    key='products',
    custom_css={'.ag-row .ag-cell': {'display': 'flex',
                                     'justify-content': 'center',
                                     'align-items': 'center'},
                '.ag-header-cell-label': {'justify-content': 'center'}}
) 

selected_rows = grid_return["selected_rows"]

if len(selected_rows):
    st.markdown('#### Selected')
    dfs = pd.DataFrame(selected_rows)

    dfsnet = dfs.drop(columns=['_selectedRowNodeInfo', 'Details'])
    AgGrid(
        dfsnet,
        enable_enterprise_modules=False,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
        reload_data=True,
        key='product_selected'
    )

with st.sidebar:
    st.subheader("MENU")
    st.markdown("""---""")

    st.write('[Rings]()')
    st.write('[Necklaces]()')
    st.write('[Bracelets]()')
    st.markdown("""---""")
