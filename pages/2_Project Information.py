import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_extras.stodo import to_do
import base64

# Create the sidebar and add the logo to it
logo = Image.open("image/logo.png")
st.sidebar.image(logo, width=200)

st.write('## Making Sense of DALRRD Commodity Prices')

st.image('image/diagram.png',use_column_width=True,caption='Solution Architectural Diagram')


#rain(emoji="🍃",font_size=54,falling_speed=5,animation_length="infinite",)
st.write("---")
st.info("General Information")
st.text("""
The South Africa DALRRD is committed to promoting equitable access to land, sustainable agriculture, and food security for all.

To achieve these goals, DALRRD requires an Agricultural Marketing Information System (AMIS)
that collects and provides daily commodity prices for horticulture, grain, and livestock.

Therefore, our project aims to automate the scraping and transformation of this data 
into a single dashboard, with relevant statistics and figures, to assist buyers and 
sellers in making informed decisions.

This data is essential for buyers and sellers to set and negotiate prices effectively.
 """)
st.write("---")


col1, col2, col3 = st.columns(3)

with col1:
   st.image("image/grains.png",use_column_width=True)
   #st.markdown("<h2 style='text-align: center; font-size: 25px;'>Grains Data</h2>", unsafe_allow_html=True)
   #st.write("### Grains Data")

   data = st.checkbox('Grains Information')
   if data:
      st.write("""
    The grains data is accessible to users through a [website](http://webapps.daff.gov.za/amis/Link.amis?method=GrainMarket). 
    
    This dataset encompasses the bids, 
    number of deals, and contracts associated with specific grains in a given market, accompanied 
    by relevant metadata about the market. 
    
    Among the produce available for sale in this market are 
    soya bean, cotton, and sorghum. Users can leverage this data to gain insights into pricing 
    dynamics, market trends, and other market-specific characteristics related to these grains.
    """)


with col2:
   st.image("image/sheep.png",use_column_width=True)
   #st.markdown("<h2 style='text-align: center; font-size: 25px;'>Livestock</h2>", unsafe_allow_html=True)
   #st.write("### Livestock")

   data = st.checkbox('Livestock Information')
   if data:
      st.write("""
    The livestock data is conveniently accessible through a [website](http://rpo.co.za/slaughtering-statistics/) and is provided in the PDF format. 

    This dataset presents comprehensive information on the total number, mass, and average price of 
    cattle, sheep, and pigs at a national level. The data is aggregated on a weekly basis, allowing 
    for a detailed analysis of the livestock market dynamics and trends. 
    
    By examining this dataset, users can gain valuable insights into the overall livestock industry, 
    including quantities, weights, and pricing patterns for cattle, sheep, and pigs at a broader scale.
    """)
   

with col3:
   st.image("image/fruits.png",use_column_width=True)
   #st.markdown("<h2 style='text-align: center; font-size: 25px;'>Horticulture</h2>", unsafe_allow_html=True)
   data = st.checkbox('Horticulture Information')
   if data:
      st.write("""
    The Horticulture data is readily accessible on a [website](http://webapps.daff.gov.za/amis/amis_price_search.jsp) and can be extracted in the popular XLS format. 
    
    This dataset offers comprehensive information regarding the quantity of horticulture produce sold 
    in a specific market on a given day, encompassing essential price statistics and metadata pertaining 
    to the market. 
    
    Some of the produce sold in this market include: apples, cabbage, apricot, pineapple,bananas, orange,etc.

    Analyzing and comprehending this data is of immense value as it allows for a thorough examination of 
    produce market trends, pricing patterns, and market-specific characteristics.
    """)
   

st.write("---")
st.subheader("Project Checklist ✅")

to_do(
    [(st.write, "Data Extraction")],
    "extract",
)
to_do(
    [(st.write, "Data Processing")],
    "process",
)
to_do(
    [(st.write, "Pipeline")],
    "pipeline",
)
to_do(
    [(st.write, "UI Interface")],
    "streamlit",
)

