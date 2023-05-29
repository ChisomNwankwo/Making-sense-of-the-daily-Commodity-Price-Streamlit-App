import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import base64
import plost
import openpyxl
from PIL import Image
from streamlit_option_menu import option_menu
from openpyxl import load_workbook



st.title('Market Price Insights')
st.info("This page offers a comprehensive view of price trends, insights, and statistics related to various horticultural products.")
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
df1 = pd.read_excel("data/cattles_sheep_processed.xlsx")
df2 = pd.read_excel("data/pigs_processed.xlsx")

#st.session_state.initialize()

st.sidebar.header("Sheep & Cattle:")
Type = st.sidebar.multiselect(
    "Select Livestock:",
    options=df1["Type"].unique(),
    default=None 
)

Class = st.sidebar.multiselect(
    "Select the Class:",
    options=df1["Class"].unique(),
    default=None 
)

#End_date = st.sidebar.date_input("Select End Date")
# Get unique dates from 'End_date' column
available_dates = df1["End_date"].unique()
End_date = st.sidebar.selectbox("Select Date", available_dates)
df1_selection = df1.query("Type == @Type & Class == @Class & End_date == @End_date")


st.sidebar.header("Pigs:")
Class = st.sidebar.multiselect(
    "Select the Class:",
    options=df2["Class"].unique(),
    default=None 
)
pig_dates = df2["End_date"].unique()
End_date = st.sidebar.selectbox("Select Date", pig_dates)
df2_selection = df2.query("Class == @Class& End_date == @End_date")


# Display filtered dataframe
st.write(df1_selection)

# Create bar chart or clustered chart for cattle & sheep data
if len(Type) == 1:
    livestock_type = Type[0].lower()
    chart1 = px.bar(df1_selection, x="Class", y="Total_Selling", color="Class")
    chart1.update_layout(title=f"Total Sales for {livestock_type.capitalize()}")
    st.plotly_chart(chart1)
elif len(Type) > 1:
    chart2 = go.Figure(data=[
        go.Bar(name="Cattle", x=df1_selection[df1_selection["Type"]=="Cattle"]["Class"], y=df1_selection[df1_selection["Type"]=="Cattle"]["Total_Selling"]),
        go.Bar(name="Sheep", x=df1_selection[df1_selection["Type"]=="Sheep"]["Class"], y=df1_selection[df1_selection["Type"]=="Sheep"]["Total_Selling"])
    ])
    chart2.update_layout(barmode="group", title="Total Sales for Cattle & Sheep")
    st.plotly_chart(chart2)

# Create bar chart or clustered chart for cattle & sheep data
if len(Type) == 1:
    livestock_type = Type[0].lower()
    chart4 = px.bar(df1_selection, x="Class", y='Avg_Mass (kg)', color="Class")
    chart4.update_layout(title=f"Average Mass per {livestock_type.capitalize()}")
    st.plotly_chart(chart4)
elif len(Type) > 1:
    chart5 = go.Figure(data=[
        go.Bar(name="Cattle", x=df1_selection[df1_selection["Type"]=="Cattle"]["Class"], y=df1_selection[df1_selection["Type"]=="Cattle"]["Total_Selling"]),
        go.Bar(name="Sheep", x=df1_selection[df1_selection["Type"]=="Sheep"]["Class"], y=df1_selection[df1_selection["Type"]=="Sheep"]["Total_Selling"])
    ])
    chart5.update_layout(barmode="group", title="Average Mass per Cattles & Sheep")
    st.plotly_chart(chart5)

st.write("---")
st.info("Market insights from our pigs livestock data")
st.write(df2_selection)

# Calculate total sales per pig class
df2_total_sales = df2_selection.groupby("Class")["Total_Purchases"].sum().reset_index()
# Create bar chart for pigs data (total sales)
chart3 = px.bar(df2_total_sales, x="Class", y="Total_Purchases", color="Class")
chart3.update_layout(title="Total Purchases for Pigs")
st.plotly_chart(chart3)

# Calculate total sales per pig class
df2_total_sales = df2_selection.groupby("Class")["Avg_Mass (kg)"].sum().reset_index()
# Create bar chart for pigs data (total sales)
chart6 = px.bar(df2_total_sales, x="Class", y='Avg_Mass (kg)', color="Class")
chart6.update_layout(title="Average Mass per Pigs")
st.plotly_chart(chart6)

st.write("---")

# Create scatter plot for correlation between Total_Purchases and Total_Selling
if len(Type) == 1:
    livestock_type = Type[0].lower()
    scatter_chart = px.scatter(df1_selection, x='Total_Purchases', y='Total_Selling', color='Class')
    scatter_chart.update_layout(title=f"Scatter Plot: Total_Selling vs Total_Purchases for {livestock_type.capitalize()}")
    st.plotly_chart(scatter_chart)
elif len(Type) > 1:
    scatter_chart = go.Figure()
    for livestock_type in Type:
        df_type = df1_selection[df1_selection["Type"] == livestock_type]
        scatter_chart.add_trace(go.Scatter(x=df_type["Total_Purchases"], y=df_type["Total_Selling"], mode='markers', name=livestock_type))
    scatter_chart.update_layout(title="Scatter Plot: Total_Selling vs Total_Purchases for Cattle & Sheep")
    st.plotly_chart(scatter_chart)


                   
