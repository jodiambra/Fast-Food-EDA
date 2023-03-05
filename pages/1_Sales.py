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

# distribution of us sales
st.subheader('US Sales')

st.write(px.histogram(df.us_sales_millions, title='Distribution of US Sales', template='ggplot2',
                      labels={'value': 'US Sales'}, color_discrete_sequence=['green'], height=700, width=900))


with st.expander('Details'):
    st.write('We see the distribution of total sales is right skewed, with most chains making less than 4.9 billion dollars.',
             'One chain in particular makes more than 45 billion dollars in sales in the US.')

st.title('')
st.title('')
#--------------------------------------------#
# distribution of unit sales 
st.subheader('Unit Sales')
st.write(px.histogram(df.average_unit_sales_thousands, title='Distribution of Average Unit Sales', template='ggplot2',
                      labels={'value': 'Average Unit Sales'}, color_discrete_sequence=['green'], height=700, width=900))
with st.expander('Details'):
    st.write('The distribution of unit sales seams to be normal, with the most values between 1.0 to 1.5 million dollars in sales.')

st.title('')
st.title('')
#-----------------------------------------#
# top sales 
st.subheader('Top Sales')
number = st.slider('Selection', min_value=10, max_value=50, step=10)
st.write(px.bar(df.sort_values(by='us_sales_millions', ascending=False).head(number), x='name', y='us_sales_millions', title='Top ' +str(number)+ ' US Sales', 
       labels={'us_sales_millions': 'Sales (millions)'}, height=700, width=900, color='name'))
with st.expander('Details'):
    st.write('McDonald\'s far exceeds the other fast food chains in terms of sales. Starbucks is second, with roughly half the total sales of',
             'Mcdonald\'s. Chick-Fil-A, Taco Bell and Wendy\'s follows close behind Starbucks')

st.title('')
st.title('')
#---------------------------------------------# 

# top unit sales 
st.subheader('Top Sales')
# uses slider from first graph
st.write(px.bar(df.sort_values(by='average_unit_sales_thousands', ascending=False).head(number), x='name', y='average_unit_sales_thousands', title='Top ' +str(number)+ ' US Unit Sales', 
       labels={'value': 'Unit Sales (thousands)'}, height=700, width=900, color='name'))
with st.expander('Details'):
    st.write('The most profitable units are found with Chick-Fil-A, Raising Cane\'s, Krispy Kreme, and Shake Shack. Surprisingly,',
             'McDonald\'s comes in 6th place.')

st.title('')
st.title('')
#------------------------------------------# 

# market share
st.subheader('Market Share')
# uses slider from first graph
st.write(px.pie(df.sort_values(by='share_of_sales', ascending=False).head(number), names='name', values='share_of_sales', title='Top ' +str(number)+ ' Market Share', 
    height=700, width=900, color='name'))
with st.expander('Details'):
    st.write('McDonald\'s dominates the market share of the fast food market, followed by Starbucks, and then Chick-Fil-A.')
