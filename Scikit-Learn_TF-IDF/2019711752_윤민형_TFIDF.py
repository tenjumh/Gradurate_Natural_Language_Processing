#!/usr/bin/env python
# coding: utf-8

# In[37]:


import json
from PyKomoran import *
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# In[38]:


komoran = Komoran("EXP")

with open('C:/Users/fxk/PycharmProjects/tenjumh/Natural_Language_Processing/NLP_Gradurate/SpeechAct.json', 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)


# In[39]:


tfidf = []
for idx, key in enumerate(data.keys()):
    text = []
    for message in data[key]:
        komoran_text = ' '.join(komoran.get_morphes_by_tags(message[1],
                                                   tag_list=['NNP', 'NNG', 'VV']))
        text.append(komoran_text)
    if len(text) == 0:
        continue
    else:
        num = idx + 1
        tfidfvect = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b', stop_words=None)
        tfidfvect.fit_transform(text)
        tfidflist = tfidfvect.transform(text).toarray().tolist()
        voca = tfidfvect.vocabulary_
        voca = sorted(voca)
        tfidf.append('(대화{})'.format(num) + '\n')
        tfidf.append(tfidflist)


# In[40]:


save_file_name = '2019711752_윤민형_TFIDF'
with open('./'+save_file_name+'.txt', 'w', encoding='utf-8', newline='') as writer_text:
    for idx, i in enumerate(tfidf):
        if idx % 2 == 0:
            writer_text.writelines(i)
        else:
            for j in i:
                for k in j:
                    k = round(k, 4)
                    writer_text.writelines(str(k) + '\t')
                writer_text.writelines('\n')
            writer_text.writelines('\n')
    print("[저장 완료]")


# In[ ]:




