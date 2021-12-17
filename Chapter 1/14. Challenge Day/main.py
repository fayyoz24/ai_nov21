import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
dataFrameSerialization = "legacy"
df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
df = df.astype(str)

st.markdown("<h1 style='text-align: center; color: white;'>FRIDAY CHALLENGE!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>OBESITY PROBLEM</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>What is Obesity? 🤔</h1>", unsafe_allow_html=True)

img = Image.open("sampl.jpg")
st.image(img, width=700)
video = open("obesity.mp4", 'rb').read()
st.video(video)

Checkbox = st.sidebar.checkbox("Reveal data")
if Checkbox:
    st.dataframe(df=df)

#st.write(df)
st.sidebar.subheader("Plotting Setup")
chart_select =st.sidebar.selectbox(
    label ="Select the chart type",
    options =['scatterplots','Lineplots', 'Histograms', 'Barchart']
)



if chart_select =='scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    gender =st.sidebar.selectbox('Gender', options=['Male',  'Female'])
    x_values = st.sidebar.selectbox('X axis', options=['Height',  'Weight'])
    y_values = st.sidebar.selectbox('Y axis', options=['Height',  'Weight'])
    plot = px.scatter(df, x = x_values, y=y_values)
    st.plotly_chart(plot)

about = st.sidebar.button("contributors")
if about:
    st.title("Fayyozjon Usmonov")
    st.title("Vishwanath Singa")
    st.title("Issifu Siaw Awudu")
    st.markdown("<h1 style='text-align: center; color: blue;'>Thanks for your attention!</h1>", unsafe_allow_html=True)
      
