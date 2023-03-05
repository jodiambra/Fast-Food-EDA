#import packages
import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image
from streamlit.commands.page_config import Layout
import numpy as np 

#----------------------------#
# Upgrade streamlit library
# pip install --upgrade streamlit

#-----------------------------#
# Page layout
icon = Image.open('images/fastfood.ico')

st.set_page_config(page_title='American Fast Food EDA',
                   page_icon=icon,
                   layout='wide',
                   initial_sidebar_state="auto",
                   menu_items=None)

image2 = Image.open('images/fast-food-assortment-soda.jpg')
st.title('American Fast Food Sales')
st.image(image2)



#---------------------------------------# 

# dataset 
df = pd.read_csv('datasets/Top 50 Fast-Food Chains in USA.csv')

# creating new features 
df['share_of_sales'] = df.us_sales_millions / df.us_sales_millions.sum(axis=0) * 100
df['company_store_ratio'] = df.company_stores / df.franchised_stores
df['franchise_store_ratio'] = df.franchised_stores / df.company_stores
df['units_percent_change'] = df.change_in_units_from_2020 / df['2021_total_units'] * 100

# replace infinity with 0
df.loc[np.isinf(df['company_store_ratio']), 'company_store_ratio'] = 0

#----------------------------------------# 

st.subheader('US Sales')

st.write(px.histogram(df.us_sales_millions, title='Distribution of US Sales', template='ggplot2',
                      labels={'value': 'US Sales'}, color_discrete_sequence=['green'], height=700, width=900))


with st.expander('Details'):
    st.write('We see the distribution of total sales is right skewed, with most chains making less than 4.9 billion dollars.',
             'One chain in particular makes more than 45 billion dollars in sales in the US.')

st.title('')
st.title('')
#--------------------------------------------#
st.subheader('Unit Sales')
st.write(px.histogram(df.average_unit_sales_thousands, title='Distribution of Average Unit Sales', template='ggplot2',
                      labels={'value': 'Average Unit Sales'}, color_discrete_sequence=['green'], height=700, width=900))
with st.expander('Details'):
    st.write('We see the distribution of total sales is right skewed, with most chains making less than 4.9 billion dollars.',
             'One chain in particular makes more than 45 billion dollars in sales in the US.')
