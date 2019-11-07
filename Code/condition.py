def condition(sen):
    nlp = spacy.load("en_core_web_sm")
    doc=nlp(sen)
    l=[(token.text,token.pos_) for token in doc if (token.pos_ == "ADV" or token.pos_=="ADJ" or token.pos_=="ADP" or token.pos_=="VERB")]
    return l
condition("How many authors wrote this paper")
