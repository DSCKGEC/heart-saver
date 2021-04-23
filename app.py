# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:18:42 2021

@author: Agni Sain
"""
from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
with open('xgb.pkl','rb') as f:
    xgb=pickle.load(f)

@app.route('/')    
def home():
    return render_template("index.html")   

    
@app.route('/predict',methods=["POST"])
def predict_heart_disease():
    
    age=request.form['age']
    sex=request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    
    pvalues=[[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    pvalues=np.array(pvalues).reshape((1,-1))
    pred=xgb.predict(pvalues)
    predf=float(pred)
    return render_template('result.html', data=predf)

@app.route('/predict_file',methods=["POST"])    
def predict_heart_disease_file():
    df_test=pd.read_csv(request.files.get("file"))
    
    prediction=xgb.predict(df_test)
    return str((list(prediction)))
    
if (__name__=='__main__'):
    app.run()

