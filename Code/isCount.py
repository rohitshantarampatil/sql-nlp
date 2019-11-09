#!/usr/bin/env python
# coding: utf-8

# In[114]:


def isCount(sentence):
    import nltk
    # nltk.download('stopwords')
    # nltk.download('punkt')
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer  
    import pandas as pd
    import numpy as np
    import re   
    import string

    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize 
    import operator
    stop_words = set(stopwords.words('english'))
    
    data = pd.read_csv("Augmented_Non_Complex.csv")
    # print(data.columns)
    natural= data.Natural.tolist()
    sql = data.SQL.tolist()
    tokenizer = RegexpTokenizer(r'\w+')

    maindict = dict()
    countdict = dict()
    for i in range(len(natural)):
        tokens = tokenizer.tokenize(natural[i].lower())
        filtered_sentence = [w for w in tokens if not w in stop_words] 
        filtered_sentence = [] 
        for w in tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w)        
        #print(filtered_sentence)
        for j in filtered_sentence:
            if j not in countdict:
                    countdict[j]=1
            else:
                    countdict[j]+=1
            if 'COUNT' in sql[i]:
                if j not in maindict:
                    maindict[j]=1
                else:
                    maindict[j]+=1
    for m in maindict:
        if countdict[m]<10:
            maindict[m] = 0
        else:
            maindict[m] =  maindict[m]/countdict[m]
    #print(maindict)

    #maindict = sorted(maindict.items(), key=operator.itemgetter(1))
    scores = []
    for i in sentence.lower().split():
        if i in maindict:
            scores.append(maindict[i])
    if max(scores)>0.9:
        return True
    else:
        return False
    
    


# In[115]:


# print(isCount("How many papers of author myman"))

