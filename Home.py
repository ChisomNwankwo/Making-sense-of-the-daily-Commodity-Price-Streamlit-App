"""

    
"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from streamlit_extras.let_it_rain import rain
from PIL import Image
import time

# Custom Libraries
#from app_functions import *

#define a function for loading css files
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    # Create the sidebar and add the logo to it
    logo = Image.open("image/logo.png")
    st.sidebar.image(logo, width=200)

    #view the page options
    #page_options = ["Home Page","Our Team","Livestock","Horticulture","Grains"]
    #page_selection = st.sidebar.selectbox("Choose Option", page_options)

    #select page options
   # if page_selection == "Home Page":
        #rain(emoji="🍃",font_size=54,falling_speed=5,animation_length="infinite",)
        # Header contents
    st.title('An Explore AI Academy Project')
    st.image('image/home.jpg',use_column_width=True)


    st.write("---")

    st.subheader("Meet the Team👨‍💼🏢👩‍💼")
    st.info("""
        Our research team is led by a highly experienced and skilled professionals, 
        who has a deep understanding of the industry and the latest trends.
        """
        )
    check1,check2,check3=st.columns(3)
    with check1:
        praise=st.checkbox("Praise Taiwo")
    with check2:
        chisom=st.checkbox("Chisom Nwankwo")

    with check3:
        simon=st.checkbox('Sello Simon')

    check4,check5,check6=st.columns(3)
    with check4:
        bukola=st.checkbox("Bukola Badeji")
    with check5:
        mbuy=st.checkbox("Mbuyiselo Mkwanazi")
    with check6:
        ben=st.checkbox("Benjamin Michael")



    if praise:
        st.image("image/Praise.png")
        st.write("Data Engineer")

    if chisom:
        st.image("image/Chisom.Png")
        st.write("Data Scientist")
    if simon:
        st.image("image/Simon.Png")
        st.write("Data Scientist")

    if bukola:
        st.image("image/Bukola.png")
        st.write("Data Engineer")

    if mbuy:
        st.image("image/Mbusela.png")
        st.write("UI Specialist")

    if ben:
        st.image("image/Michael.png")
        st.write("Data Scientist")

    st.write('---')
    st.subheader('News 📰')
    image,text=st.columns(2)
    with image:
        st.image("image/potatoes.jpg")
    with text:
        st.write("#### ‘Duties will protect potato industry against unfair trade’")
        st.write(
            """
            Government recently approved anti-dumping duties, ranging between 
            8,8% to 239%, on frozen potato chips imported from the Netherlands, 
            Germany and Belgium.
            """
            )
        st.markdown("[see more](https://www.farmersweekly.co.za/agri-news/south-africa/duties-will-protect-potato-industry-against-unfair-trade/)")

    image1,text1=st.columns(2)
    with image1:
        st.image("image/farm.jpg")
    with text1:
        st.write("#### Africa is the next big export market opportunity for Irish firms") 
        st.write(
            """
           Despite Challenges, there are significant and 
           expanding commercial opportunities for Irish enterprises in key African 
           markets like Ghana, Kenya, Nigeria, and South Africa.
            """
            )
        st.markdown("[see more](https://www.independent.ie/business/irish/africa-is-the-next-big-export-growth-market-opportunity-for-irish-firms-as-demand-for-goods-and-services-rises/a1815948857.html)")



    st.write('---')

    st.subheader("📬 Get in Touch with us!")
    contact_form = """
        <form action="https://formsubmit.co/cynthiarapheals@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message"></textarea>
     <button type="submit">Send</button>
</form>
					"""
    st.markdown(contact_form, unsafe_allow_html = True)
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    local_css("style.css")





# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
 