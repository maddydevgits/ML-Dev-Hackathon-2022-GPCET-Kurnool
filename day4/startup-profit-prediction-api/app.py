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
    return ('Data Collected')

if (__name__=="__main__"):
    app.run()











