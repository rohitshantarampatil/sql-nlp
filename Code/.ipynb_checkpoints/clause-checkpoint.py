{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List titles of all the papers\n",
      "['List', 'titles', 'all', 'papers']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['Title', 'PaperID']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import difflib\n",
    "from fuzzywuzzy import process\n",
    "import re\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "#Natural language is direct query with no edits\n",
    "#return the cluases from the natural language\n",
    "\n",
    "def clause(Natural,colnames):\n",
    "    clause=[]\n",
    "    token=re.split('\\s|(?<!\\d)[,.?](?!\\d)', Natural)\n",
    "    i=0\n",
    "    stop_words = set(stopwords.words('english'))\n",
    "    while(i<len(token)):\n",
    "        if(token[i]==\"\" or token[i] in stop_words):\n",
    "            token.pop(i)\n",
    "        i+=1\n",
    "    print(token)\n",
    "    for str2match in token:\n",
    "    # You can also select the string with the highest matching percentage\n",
    "        highest = process.extractOne(str2match,colnames)\n",
    "        if(highest[1]>=75):\n",
    "            clause.append(highest[0])\n",
    "    return clause\n",
    "colnames=['AffiliationID', 'KeywordID', 'FieldID', 'Name', 'Summary', 'Place', 'Venue', 'Year', 'ConfID', 'Affiliation', 'PaperID', 'Title', 'Topic', 'AuthID']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
