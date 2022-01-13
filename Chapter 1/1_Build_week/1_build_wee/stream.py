import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
from difflib import get_close_matches


st.markdown("<h1 style='text-align: center; color: blue;'>Billionaries spend their main time for books!</h1>", unsafe_allow_html=True)
img = Image.open("Boy-looking-at-Books.jpg")
st.image(img, width=700)

df = pd.read_csv('The_best.csv', index_col=0)
df = df[['Titles', 'Authors','Pages','Years', 'Places','The_Numbers_of_awards','Awards','Series','Reviews', 'Votes', 'Average_rating',
       'Number_of_Rated_people','Urls']]


data_ = st.sidebar.radio(
     label="Do you want to see the whole data?",
     options=("No",'Yes'))

if data_ == 'Yes':
    st.markdown("<h1 style='text-align: center; color: white;'>The top 1000 books!</h1>", unsafe_allow_html=True)
    st.write(df)

path = st.sidebar.text_input('Search for your book!!!')
if path:
    matches = list(get_close_matches(path, df['Titles'].values))
    st.text('That is the best choice!')
    st.write(df.loc[df['Titles'].isin(matches)])

st.sidebar.subheader("Choose the top books")
top_book_ = st.sidebar.selectbox(
    label ="Select the top books",
    options = [5, 10, 50, 100])
                            

st.sidebar.subheader("Choose the tops by...")
top_book_sel =st.sidebar.selectbox(
    label ="Select the top books",
    options =['The_Numbers_of_awards','Reviews', 'Votes', 'Average_rating',
       'Number_of_Rated_people','Pages'])


df_sorted = df.sort_values(by=[top_book_sel], ascending=False)
                           
confirm = st.sidebar.checkbox('confirm')
if confirm:
     st.write(df_sorted.head(top_book_))


# if chart_select =='scatterplots':
#     st.sidebar.subheader("Scatterplot Settings")
#     gender =st.sidebar.selectbox('Gender', options=['Male',  'Female'])
#     x_values = st.sidebar.selectbox('X axis', options=['Height',  'Weight'])
#     y_values = st.sidebar.selectbox('Y axis', options=['Height',  'Weight'])
#     plot = px.scatter(df, x = x_values, y=y_values)
#     st.plotly_chart(plot)
