# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:18:42 2021

@author: Agni Sain
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

#data=pd.read_csv("D:\heart-saver\flaskApp\heart-saver.csv")
app=Flask(__name__)
with open('xgb.pkl','rb') as f:
    xgb=pickle.load(f)

@app.route('/')    
def welcome():
    return 'Welcome All'   

    
@app.route('/predict')
def predict_heart_disease():
    age=request.args.get('age')
    sex=request.args.get('sex')
    cp = request.args.get('cp')
    trestbps = request.args.get('trestbps')
    chol = request.args.get('chol')
    fbs = request.args.get('fbs')
    restecg = request.args.get('restecg')
    thalach = request.args.get('thalach')
    exang = request.args.get('exang')
    oldpeak = request.args.get('oldpeak')
    slope = request.args.get('slope')
    ca = request.args.get('ca')
    thal = request.args.get('thal')
    
    pvalues=[[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    pvalues=np.array(pvalues).reshape((1,-1))
    pred=xgb.predict(pvalues)
    return str(pred)

@app.route('/predict_file',methods=["POST"])    
def predict_heart_disease_file():
    df_test=pd.read_csv(request.files.get("file"))
    
    prediction=xgb.predict(df_test)
    return str((list(prediction)))
    
if (__name__=='__main__'):
    app.run()

