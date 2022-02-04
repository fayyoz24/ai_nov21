import streamlit as st
import data_handler as dh
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
from difflib import get_close_matches
from sklearn.preprocessing import StandardScaler as scaler

from data_handler import preprocess
from train import Models
from sklearn.svm import SVC

st.markdown("<h1 style='text-align: center; color: blue;'>You can not live without HEART!...</h1>", unsafe_allow_html=True)
img = Image.open("heart.jpg")
st.image(img, width=700)

df = pd.read_csv('heart.csv', index_col=0)

data_ = st.sidebar.radio(
    label="Do you want to see the whole data?",
    options=("No",'Yes'))

if data_ == 'Yes':
    st.markdown("<h1 style='text-align: center; color: white;'>The top 1000 books!</h1>", unsafe_allow_html=True)
    st.write(df)


st.sidebar.subheader("Alghorithms")
top_book_ = st.sidebar.selectbox(
    label ="Select your Algorithm",
    options = ['SVC','LogisticRegression','RandomForestClassifier','KNeighborsClassifier',
    'GradientBoostingClassifier','XGBClassifier','DecisionTreeClassifier'])

models = [Models.svc(), Models.lr(), Models.rfc(), Models.knc(), Models.gbc(), Models.xgbc(), Models.dtc()]

a = ['SVC','LogisticRegression','RandomForestClassifier','KNeighborsClassifier',
    'GradientBoostingClassifier','XGBClassifier','DecisionTreeClassifier']

if top_book_ :
    st.text('''
    
    

    ''')
    st.write(models[a.index(top_book_)])


user_input = st.sidebar.radio(
    label="Do you want to know about your healthy?",
    options=("No",'Yes'))

if user_input == 'Yes':
    
    age = st.text_input("How old are you? \n")

    sex_ = st.radio(label='Choose your gender', options=('Male', 'Female'))
    if sex_ == 'Male':
        sex = 1
    else:
        sex = 0
    
    cp = st.radio(label='Choose your CP', options=(0,1,2,3))

    trtbps = st.text_input("Enter yout TRTBPS\n")

    chol = st.text_input("Enter your CHOL \n")

    fbs = st.radio(label='Choose your FBS', options=(0,1))

    restecg = st.radio(label='Choose your RESTESG', options=(0,1,2))

    thalc = st.text_input("Enter your THALAShC \n")

    exng = st.radio(label='Choose your EXNG', options=(0,1))

    oldpeak = st.text_input("Enter your OLDPEAK \n")

    slp = st.radio(label='Choose your SLP', options=(0,1,2))

    caa = st.radio(label='Choose your CAA', options=(0,1,2,3, 4))

    thall = st.radio(label='Choose your THALL', options=(0,1,2,3))

    x = pd.DataFrame({"age":age, "sex":sex, 'cp':cp, 'trtbps':trtbps, 'chol':chol, 'fbs':fbs, 'restecg':restecg, 'thalachh':thalc,
        'exng':exng, 'oldpeak':oldpeak, 'slp':slp, 'caa':caa, 'thall':thall}, index=[0])

    X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')
    X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')
    model1 = SVC(kernel='rbf')
    model1.fit(X_train_scaled, y_train)

    predictions = np.array([model1.predict(x)])
    if predictions==0:
        st.markdown("<h3 style='text-align: center; color: blue;'>You are Healthy!!!</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center; color: blue;'>Please go to the doctor...\n I got POSITIVE result</h3>", unsafe_allow_html=True)

about = st.sidebar.button("contributors")
if about:
    st.title("Fayyozjon Usmonov")
    st.markdown("<h1 style='text-align: center; color: blue;'>Thanks for your attention!</h1>", unsafe_allow_html=True)