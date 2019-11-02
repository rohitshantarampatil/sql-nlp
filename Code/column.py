import pandas as pd
import spacy
from spacy import displacy
from difflib import get_close_matches

def give_column(sen_without_ne):#column_names=['Place','Affiliate','AffiliationID','AuthID','FieldID','Name','ConfID','PaperID','Venue','Year','Topic','KeywordID','Summary','Title']
    column_names=['Place','Affiliate','AffiliationID','AuthID','FieldID','Name','ConfID','PaperID','Venue','Year','Topic','KeywordID','Summary','Title']
    lower_column_names=[]
    for i in column_names:
        lower_column_names.append(i.lower())
    nlp = spacy.load("en_core_web_sm")
    doc=nlp(sen_without_ne)
    l=[token.text for token in doc if (token.pos_ == "NOUN" or token.pos_=="PROPN")]
    # print(l)
    a=[]
    x=[]
    for i in l:
        x=get_close_matches(i.lower(), lower_column_names,n=1,cutoff=0.5)
        if not x==[]:
            for j in range(len(lower_column_names)):
                if lower_column_names[j]==x[0]:
                    a.append(column_names[j])
                    break
                else:
                    continue
        # else:
        #     print('error')
    return list(set(a))
print(give_column("How many papers were published in the year at  Proceedings of the Eighth Workshop on Asian Language Resouces How many papers were published in the year at  Proceedings of the Eighth Workshop on Asian Language Resouces "))