import pandas as pd
import spacy
from spacy import displacy
from difflib import get_close_matches
def give_column(sen_without_ne,column_names):#column_names=['Place','Affiliate','AffiliationID','AuthID','FieldID','Name','ConfID','PaperID','Venue','Year','Topic','KeywordID','Summary','Title']
    lower_column_names=[]
    for i in column_names:
        lower_column_names.append(i.lower())
    nlp = spacy.load("en_core_web_sm")
    doc=nlp(sen_without_ne=_without_ne)
    l=[token.text for token in doc if (token.pos_ == "NOUN" or token.pos_=="PROPN")]
    a=[]
    x=[]
    for i in l:
        x=get_close_mathches(i.lower(), lower_column_names,n=1,cutoff=0.46)
        if not x==[]:
            a.append(x)
        else:
            print('error')
    return a