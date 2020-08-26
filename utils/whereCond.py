import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import tensorflow as tf
import pandas as pd
import numpy as np
from preprocess import makeRawDataset,removePunc,fuzzy,encode
from sklearn.model_selection import train_test_split
import nltk
import string
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier,Booster,DMatrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

def train(file):
    y_data=makeRawDataset(file) #provides with raw data
    X=pd.read_csv(file).Question
    X_without=removePunc(X) #without punctuations
    X_correct=fuzzy(X_without) #with fuzzy
    X_enc=encode(X_correct)
    labels=[">","<","<=",">=","==","NULL","LIKE"]
    encoder=LabelEncoder()
    codes=encoder.fit_transform(labels)
    codeMap={labels[i]:codes[i] for i in range(len(labels))}
    inverseMap={codes[i]:labels[i] for i in range(len(labels))}
    maps={"codeMap":codeMap,"inverseMap":inverseMap}
    np.save("Map.npy",maps)
    y=[]
    for i in y_data:
        y.append(codeMap[i])
    X_train, X_test, y_train, y_test = train_test_split(X_enc, y, test_size = 0.2, random_state = 42)
    model = XGBClassifier()
    model.fit(X_train,y_train)
    model.save_model("WhereCond.model")
    y_hat=model.predict(X_test)
    print(y_hat[:10])
    y_pred=[]
    for i in y_hat:
        y_pred.append(inverseMap[i])
    y_true=[]
    for i in y_test:
        y_true.append(inverseMap[i])
    sk_report = classification_report(digits=6,y_true=y_test,y_pred=y_hat)
    print(sk_report)
def test(x,modelFile):
    model = Booster() #init model
    model.load_model(modelFile) # load data
    maps=np.load("Map.npy",allow_pickle=True)
    x_enc=encode([x])
    y_enc=model.predict(DMatrix(x_enc))
    y_pred=np.argmax(y_enc)
    inverseMap=maps.item().get("inverseMap")
    y_hat=inverseMap[y_pred]
    print(y_hat)
