import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from flask import Flask,request

app=Flask(__name__)

dataset=pd.read_csv('50_Startups_MLR.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X=ct.fit_transform(X)
print(X)
regressor=LinearRegression()
regressor.fit(X,Y)

@app.route('/predict',methods=['GET'])
def getData():
    rd=request.args.get('rd')
    a=request.args.get('a')
    m=request.args.get('m')
    s=request.args.get('s')
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
    return (str(out))

if (__name__=="__main__"):
    app.run()











