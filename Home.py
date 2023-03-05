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

home = Image.open('images/fast food.jpg')
st.title('American Fast Food EDA')
st.image(home)

st.write('This Project explores American fast food chains, through sales, market share, and the number of restaurant locations.',
        'The data will illustrate the king of fast food, and which chains are dying off.')

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