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
    rd=float(request.form['rd'])
    a=float(request.form['a'])
    m=float(request.form['m'])
    s=request.form['s']
    print(rd,a,m,s)
    b1=0
    b2=0
    b3=0
    if(s.lower()=='florida'):
        b1=0
        b2=1
        b3=0
    elif(s.lower()=='new york'):
        b1=0
        b2=0
        b3=1
    elif(s.lower()=='california'):
        b1=1
        b2=0
        b3=0

    out=regressor.predict([[b1,b2,b3,rd,a,m]])[0]
    return(render_template('index.html',result=out))

if(__name__=="__main__"):
    app.run()




