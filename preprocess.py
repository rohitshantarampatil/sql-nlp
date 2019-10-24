import pandas as pd
import numpy as np
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
