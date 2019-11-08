#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import string
import re
# from bert_serving.client import BertClient
# bc = BertClient()
# Data_Final=pd.read_csv("/Users/prakash/Desktop/natural-to-sql/Final_Processed/Augmented.csv")
arr=["AffiliationID_Place_Affiliation.csv","AuthID_AffiliationID.csv","AuthID_FieldID.csv","AuthID_Name.csv"
     ,"ConfID_FieldID.csv","ConfID_PaperID.csv","ConfID_Venue_Year.csv","FieldID_Topic.csv","KeywordID_PaperID.csv"
     ,"PaperID_AuthID.csv","PaperID_FieldID.csv","PaperID_Summary.csv","PaperID_Title.csv"]
maping={}
table={}
for i in range(13):
    data=pd.read_csv("/Users/prakash/Desktop/natural-to-sql/Dataset/"+arr[i])
    table[arr[i]]=data.columns
    for val in data.columns:
        if(val in maping):
            maping[val]=list(set(data[val]).intersection(set(maping[val])))
        else:
            maping[val]=list(set(data[val]))
    maping['NUM']=[str(i) for i in range(1000)]

def NER(natural):
    tempo=natural
    colname_identity=[]
#     tempo=re.sub(r'[^a-zA-Z \']+', '',tempo)
    while(tempo.find('\'')!=-1):
        start=tempo.find('\'')
        if(tempo.find('\'',start+1)!=-1):
            end=tempo.find('\'',start+1)
            ele=tempo[start+1:end]
#             print(ele)
            for key in maping:
                for value in maping[key]:
                    if(ele==value):
                        tempo=tempo[:start].strip()+" "+tempo[end+1:].strip()
                        colname_identity.append([key,ele])
#     print(tempo)
    token=re.split('[,.?\'\'\" ]', tempo)
    #     print(token)
    for ele in token:
        for key in maping:
            for value in maping[key]:
                if(ele==value):
                    colname_identity.append([key,ele])
                    token.remove(ele)
    processed_natural=" ".join(token)
    return (colname_identity,processed_natural)

