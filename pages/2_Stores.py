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

image1 = Image.open('images/fast-food-restaurant-signs.jpg')
st.title('Store Units')
st.image(image1)

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

st.title('')
st.title('')
#----------------------------------------# 

# distribution of unit sales 
st.subheader('Unit Sales')
st.write(px.histogram(df['2021_total_units'], title='Distribution of Total Units', template='ggplot2',
                      labels={'value': 'Total Store Units'}, color_discrete_sequence=['green'], height=700, width=900))
with st.expander('Details'):
    st.write('The distribution of total store units in 2021')

st.title('')
st.title('')
#----------------------------------------------#
# total number of stores
st.subheader('Total Number of Stores')
st.write(px.bar(df, x='name', y=['franchised_stores', 'company_stores'], title='Total Number of Stores',
                labels={'value': 'Number of Stores'}, height=700, width=1200))

with st.expander('Details'):
    st.write('The fast food chains with the most number of stores are Subway, Starbucks, and then McDonald\'s.')

st.title('')
st.title('')

#----------------------------------------#
# top number of stores 
st.subheader('Top Number of Stores')
number = st.slider('Selection', min_value=10, max_value=50, step=10)
st.write(px.bar(df.sort_values(by='2021_total_units', ascending=False).head(number), x='name', y='2021_total_units', title='Top '+str(number)+ ' Total Number of Stores',
                 labels={'total_stores': 'Number of Stores'}, height=800, width=1300, color='name'))
with st.expander('Details'):
    st.write('Subway chains outnumber the other fast food chains in the total number of locations in 2021. They are followed by',
             'Starbucks and McDonald\'s locations.')
    
st.title('')
st.title('')
#-----------------------------------------# 

if st.button('Percent Changes'):
    # Unit Percent Changes
    st.subheader('Unit Percent Change')
    st.write(px.bar(df, x='name', y='units_percent_change', height=800, title='Unit Percent Change', 
                labels={'units_percent_change': '% Change'}, width=1300))
    with st.expander('Details'):
        st.write('We see that Subway lost 1043 units in 2021, while other chains saw small losses, or a few hundred new units. Jersey Mike\'s and',
             'McDonald\'s saw the most new units.')
else:

    # unit changes
    st.subheader('Change in Units')
    st.write(px.bar(df, x='name', y='change_in_units_from_2020', height=800, title='Change in Units', width=1300,
                    labels={'change_in_units_from_2020': 'Units'}))
    with st.expander('Details'):
        st.write('We see that Subway lost 1043 units in 2021, while other chains saw small losses, or a few hundred new units. Jersey Mike\'s and',
                'McDonald\'s saw the most new units.')
    
st.title('')
st.title('')
#---------------------------------------#

# Unit Percent Changes
if st.button('Company/Franchise Ratio'):
    st.subheader('Company vs Franchise Ratio')
    st.write(px.bar(df, x='name', y='company_store_ratio', height=800, width=1300, title='Company/Franchise Store Ratio', 
                    labels={'company_store_ratio': 'Company/Franchise Ratio'}, color='name'))
    with st.expander('Details'):
        st.write('Raising Cane\'s has the highest ratio of company owned locations to franchises. Second is Panda Express, and then Shake Shack.')
else:
    st.subheader('Franchise vs Company Ratio')
    st.write(px.bar(df, x='name', y='franchise_store_ratio', height=800, width=1300, title='Franchise/Company Store Ratio', 
       labels={'franchise_store_ratio': 'Franchise/Company Ratio'}, color='name'))
    with st.expander('Details'):
        st.write('Dairy Queen has the greatest franchise ratio, followed by Tropical Smoothie Cafe, and then Moe\'s.')

st.title('')
st.title('')
#---------------------------------------#