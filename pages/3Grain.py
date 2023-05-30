import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import plost
import openpyxl
from PIL import Image
from streamlit_option_menu import option_menu



st.title('Market Price Insights')
st.info("This page offers a comprehensive view of price trends, insights, and statistics related to various grain products.")
#Place logo on top left corner of navbar
st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="10% 0%",
    margin_top="0%",
    image_width="35%",
    image_height="30%"
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("pics/logo.png")

#Load livestock data 
df = pd.read_excel("data/grains_processed.xlsx")

#st.session_state.initialize()

st.sidebar.header("Grains:")

Type = st.sidebar.multiselect(
    "Select Contract:",
    options=df["contract_type"].unique(),
    default=None  # Remove the default index selection
)

Class = st.sidebar.multiselect(
    "Select the Market:",
    options=df["market"].unique(),
    default=None  # Remove the default index selection
)

df = df.query("contract_type == @Type & market == @Class")



st.write(df)
st.write("---")

# Calculate total sales per contract
df_total_sales = df.groupby("contract_type")["total_sales"].sum().reset_index()
# Create bar chart 
chart = px.bar(df_total_sales, x="contract_type", y="total_sales", color="contract_type")
chart.update_layout(title="Total Sales per Contract Type")
st.plotly_chart(chart)

st.write("---")
##create line graph
# Sort the data by date
df.sort_values(by="date", inplace=True)
line_chart = px.line(
    df,
    x="date",
    y="total_sales",
    title="Total Sales Over Time",
    template="plotly_white"
)
# Display the line chart in Streamlit
st.plotly_chart(line_chart)

st.write("---")
#df_offers = df_selection.groupby("contract_type")["offer"].sum().reset_index()
# Create pie chart 
pie_chart = px.pie(df,
                   title=("Contracts for Produces"),
                   values="contract",
                   names="contract_type")
st.plotly_chart(pie_chart)