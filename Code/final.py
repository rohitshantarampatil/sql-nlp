#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from NER import NER
from Graph import from_query
import pandas as pd
import spacy
from spacy import displacy
from difflib import get_close_matches
from column import give_column
from isCount import isCount
def remove_(select,where):
    res=[ele if ele not in where else None for ele in select]
    while(None in res):
        res.remove(None)
    return res
def main(sen):#data_file="Augmented_Non_Complex.csv"
    Data_Final=pd.read_csv("Augmented_Non_Complex.csv")
    N=pd.DataFrame([sen])
    Natural=N[0]
    Natural_after_NER=list(map(lambda x: NER(x)[1],Natural))
    Where_Clause=list(map(lambda x: NER(x)[0],Natural))
    Select_Clause=list(map(give_column,Natural_after_NER))
    Is_Count=list(map(isCount,Natural_after_NER))
    Select_Clause_Processed=[]
    for i in range(len(Select_Clause)):
        if(Is_Count[i]):
            if(Where_Clause[i]==[]):
                Select_Clause_Processed.append(Select_Clause[i])
                query,first_table,last_table=from_query(Select_Clause_Processed[i][0],Select_Clause_Processed[i][0])
                print("SELECT DISTINCT COUNT(*) ",query,sep='')
            else:
                Select_Clause_Processed.append(remove_(Select_Clause[i],Where_Clause[i][0][0]))
    #         print(Select_Clause_Processed[i][0],Where_Clause[i][0][0])
                query,first_table,last_table=from_query(Select_Clause_Processed[i][0],Where_Clause[i][0][0])
                print("SELECT DISTINCT COUNT(*) ",query," WHERE ",last_table+'.'+Where_Clause[i][0][0],"=","'",Where_Clause[i][0][1],"'",sep='')
        else:
            if(Where_Clause[i]==[]):
                Select_Clause_Processed.append(Select_Clause[i])
                query,first_table,last_table=from_query(Select_Clause_Processed[i][0],Select_Clause_Processed[i][0])
                print("SELECT DISTINCT ",first_table,".",Select_Clause_Processed[i][0]," ",query,sep='')
            else:
                Select_Clause_Processed.append(remove_(Select_Clause[i],Where_Clause[i][0][0]))
#             print(Select_Clause_Processed[i])
                if(len(Select_Clause_Processed[i])==0):
                    print("Fuck")
                else:
    #         print(Select_Clause_Processed[i][0],Where_Clause[i][0][0])
                    query,first_table,last_table=from_query(Select_Clause_Processed[i][0],Where_Clause[i][0][0])
                print("SELECT DISTINCT ",first_table,".",Select_Clause_Processed[i][0]," ",query," WHERE ",last_table+'.'+Where_Clause[i][0][0],"=","'",Where_Clause[i][0][1],"'",sep='')

