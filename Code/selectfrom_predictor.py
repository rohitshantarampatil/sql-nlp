#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import re
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
from bert_serving.client import BertClient
def natural_language_to_embeddings(dataset_file):#dataset in a CSV File format
    args = get_args_parser().parse_args(['-model_dir', 'C:\\Users\\Ronak\\Desktop\\uncased_L-12_H-768_A-12','-port', '5555','-port_out', '5556','-max_seq_len', 'NONE', '-mask_cls_sep','-cpu'])
    server = BertServer(args)
    server.start()
    bc = BertClient()
    df=pd.read_csv(dataset_file)
    l=df.values.tolist()
    nat_lan_sen=[]
    for i in l:
        nat_lan_sen.append(i[0])
    sen_encodings=bc.encode(nat_lan_sen)
    return sen_encodings
def train_step1predictor(sen_encodings,dataset_file): #sentence encodings as list,dataset in a CSV file format
    df=pd.read_csv(dataset_file)
    l=df.values.tolist()
    data=[]
    c=[]
    f=[]
    for i in range(len(l)):
        f=re.findall(r'SELECT (.*?) FROM',l[i][1],re.I)
        if f!=[]:
            c.append(f[0])
        else:
            c.append('wrong')
    df_trueclass=pd.DataFrame({'class':c})
    df_encodings=pd.DataFrame(sen_encodings)
    X=df_encodings
    y=df_trueclass
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=72)
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    rfc_predict = rfc.predict(X_test)
    print(confusion_matrix(y_test, rfc_predict))
    print(classification_report(y_test, rfc_predict))
    with open('step1_model.pkl', 'wb') as f:
        pickle.dump(clf, f)
def table_column_predictor(input_sentence,model_file): #model from pickle file
    with open(model_file, 'rb') as f:
        clf = pickle.load(f)
        return clf.predict(input_sentence)


# In[ ]:




