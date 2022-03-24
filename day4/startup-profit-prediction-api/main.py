import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,request

app=Flask(__name__)

dataset=pd.read_csv('50_Startups_MLR.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X=ct.fit_transform(X)
print(X)
regressor=LinearRegression()
regressor.fit(X,Y)

@app.route('/')
def homePage():
    return(render_template('index.html'))

@app.route('/predict',methods=['POST'])
def collectData():
    rd=request.form['rd']
    a=request.form['a']
    m=request.form['m']
    s=request.form['s']
    print(rd,a,m,s)
    return(render_template('index.html'))

if(__name__=="__main__"):
    app.run()




