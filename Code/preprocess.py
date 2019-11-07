import pandas as pd
import numpy as np
from bert_serving.client import BertClient
import string
from fuzzywuzzy import process

columnNames=["AffiliationID","Place","Affiliation","AuthID","FieldID","Paper","Authors","Conference","Name","Affiliate"
             "ConfID","PaperID","Venue","Year","Topic","KeywordID","Summary","Title"]
columnNames.extend([i.lower() for i in columnNames])
def makeRawDataset(s):
    data=pd.read_csv(s)
    sub="WHERE"
    ind=data["SQL"].str.find(sub)
    y=[]
    for i in range(len(data.SQL)):
        if ind[i]==-1:
            y.append("NULL")
        else:
            # print(type(data.loc[i,"SQL"]))
            doubleEquals=data.loc[i,"SQL"].find("==",ind[i])
            singleEquals=data.loc[i,"SQL"].find("=",ind[i])
            greater=data.loc[i,"SQL"].find(">",ind[i])
            greaterEquals=data.loc[i,"SQL"].find(">=",ind[i])
            lesser=data.loc[i,"SQL"].find("<",ind[i])
            lesserEquals=data.loc[i,"SQL"].find("<=",ind[i])
            LIKE=data.loc[i,"SQL"].find("LIKE",ind[i])
            if(doubleEquals!=-1):
                y.append("==")
            elif(greaterEquals!=-1):
                y.append(">=")
            elif(lesserEquals!=-1):
                y.append("<=")
            elif(greater!=-1):
                y.append(">")
            elif(lesser!=-1):
                y.append("<")
            elif(singleEquals!=-1):
                y.append("==")
            elif(LIKE!=-1):
                y.append("LIKE")
            else:
                y.append("Other")
    # print(y)
    return y
# print(makeRawDataset("NLP_Dataset.csv"))
def removePunc(X):
    stop_word=set(string.punctuation)
    X_without=[]
    for i in X:
        temp=i.split()
        X_without.append([j for j in temp if j not in stop_word])
    return X_without
def fuzzy(X_without):
    X_correct=[]
    for i in range(len(X_without)):
        temp_s=[]
        for j in range(len(X_without[i])):
            if process.extractOne(X_without[i][j],columnNames)[1]<75 and '$' not in X_without[i][j]:
                temp_s.append(X_without[i][j])
        if(len(temp_s)):
            temp_s=" ".join(i for i in temp_s)
            if(temp_s[-1] in string.punctuation):
                X_correct.append(temp_s[:-1])
            else:
                X_correct.append(temp_s)
        else:
            X_correct.append("None")
    return X_correct
def encode(X_correct):
    bc = BertClient()
    if(type(X_correct)==type([])):
        X_enc=bc.encode(X_correct)
    else:
        X_enc=bc.encode(list(X_correct))
    return X_enc