import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.header('Diabetes Prediction System')

dataset=pd.read_csv('diabetes.csv')

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

classifier = LogisticRegression()
classifier.fit(X,Y)

p=st.text_input('Enter Pregnancies')
g=st.text_input('Enter Glucose')
bp=st.text_input('Enter Blood Pressure')
s=st.text_input('Enter Skin Thickness')
i=st.text_input('Enter Insulin')
bmi=st.text_input('Enter BMI')
dpf=st.text_input('Enter DPF')
age=st.text_input('Enter Age')

if st.button('Predict Diabetes'):
    out=classifier.predict([[p,g,bp,s,i,bmi,dpf,age]])[0]
    if(out==0):
        st.success('No Diabetes')
    else:
        st.warning('Diabetes Found')
