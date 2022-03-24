import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

st.header('Crop Prediction System')

dataset=pd.read_csv('crop.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
classifier=KNeighborsClassifier()
classifier.fit(X_train,Y_train)
Y_pred=classifier.predict(X_test)
print(accuracy_score(Y_pred,Y_test))

N=(st.text_input('Enter Nitrogen'))
P=(st.text_input('Enter Phosphorous'))
K=(st.text_input('Enter Potassium'))
T=(st.text_input('Enter Temperature'))
H=(st.text_input('Enter Humidity'))
PH=(st.text_input('Enter pH'))
R=(st.text_input('Enter Rainfall'))

if st.button('Predict Crop'):
    crop=classifier.predict([[N,P,K,T,H,PH,R]])[0]
    st.success(crop)