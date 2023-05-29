import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import plost
import openpyxl
from PIL import Image
from streamlit_option_menu import option_menu

# DATABASE SYNC CODE
# from sqlalchemy import create_engine, text


# # Transmit data from RDS INstance
# # create sqlalchemy engine
# engine = create_engine("mysql+pymysql://{user}:{pw}@intern-dalrrd-team9-database.ctgb19tevqci.eu-west-1.rds.amazonaws.com/{db}"
#                        .format(user="explore_student",
#                                pw="explore-student",
#                                db="darrld_data"))

# # Establish a connection to the database
# conn = engine.connect()

# # Query the table and assign the result to grain_db_df
# query = text("SELECT * FROM horticulture_data")
# horticulture_db_df = pd.read_sql(query, con=conn) # Here is your horticulture data

# # Close the database connection
# conn.close()

st.title('Horticulture Market Price Insights')
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
    image_height="30%",
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

#load horticulture dataset
@st.cache_data
#@st.cache_resource
def get_data_from_excel():
    hort = pd.read_excel("data/horticulture_processed.xlsx",
           engine = "openpyxl", 
)
    return hort
hort = get_data_from_excel()
    
#st.session_state.initialize()

st.sidebar.header("Horticulture:")
city = st.sidebar.multiselect(
    "Select the City:",
    options = hort["Market"].unique(),
    default = None   
)
    
product = st.sidebar.multiselect(
    "Select the Product:",
    options = hort["Product"].unique(),
    default=None 
)
    
product_type = st.sidebar.multiselect(
    "Select the Class:",
    options = hort["Class"].unique(),
    default=None 
)

product_size = st.sidebar.multiselect(
    "Select the Size:",
    options = hort["Size"].unique(),
    default=None 
)

hort_selection = hort.query(
    "Market == @city & Class == @product_type & Product == @product & Size == @product_size"
)


#product rating
total_sales = int(hort_selection["Total Sales(Rand)"].sum())
average_closing_stock = round(hort_selection["Closing Stock"].mean(), 1)
average_price_by_product = round(hort_selection["Average Price"].mean(), 2)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"**Total Sales(Rand):**")
    st.markdown(f"**ZAR R {total_sales:,}**")
with c2:
    st.markdown("**Average Price Per Product:**")
    st.markdown(f"**ZAR R {average_price_by_product}**")
with c3:
    st.markdown(f"**Average Stock Price:**")
    st.markdown(f"**ZAR R {average_closing_stock}**")

st.write(hort_selection)
        
st.markdown("---")
                  
# Total sales by product (bar chart)
df_total_sales = hort_selection.groupby("Product")["Total Sales(Rand)"].sum().reset_index()
# Create bar chart 
chart1 = px.bar(df_total_sales, x="Product", y="Total Sales(Rand)", color="Product")
chart1.update_layout(title="Total Sales by Produce")
st.plotly_chart(chart1)

st.markdown("---")

#products by popularity
pie_chart = px.pie(hort_selection,
                   title=("Product Popularity"),
                   values="Sales Quantity",
                   names="Product")
st.plotly_chart(pie_chart)

st.write("---")
# price trends of the horticulture produce
# daily sales by product (bar chart)
df_daily_sales = hort_selection.groupby("Product")["Average Price"].sum().reset_index()
# Create bar chart 
chart2 = px.bar(df_daily_sales, x="Product", y="Average Price", color="Product")
chart2.update_layout(title="Daily price for  Produces")
st.plotly_chart(chart2)

st.write("---")
# Sort the data by date
hort_selection.sort_values(by="Date", inplace=True)
# Create the line chart
line_chart = px.line(
    hort_selection,
    x="Date",
    y="Total Sales(Rand)",
    title="Total Sales Over Time",
    template="plotly_white"
)
# Display the line chart in Streamlit
st.plotly_chart(line_chart)

