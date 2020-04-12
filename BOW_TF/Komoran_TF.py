#!/usr/bin/env python
# coding: utf-8

# In[149]:


import json
from PyKomoran import *
import csv
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해

komoran = Komoran("EXP")

with open('C:/Users/fxk/PycharmProjects/tenjumh/Natural_Language_Processing/NLP_Gradurate/SpeechAct.json', 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)


# In[150]:


document = []
for key in data.keys():
    #docs.append([])
    text = []
    #print('---------------')
    for message in data[key]:
        komoran_text = komoran.get_morphes_by_tags(message[1],
                                                   tag_list=['NNP', 'NNG', 'VV'])
        text.append(komoran_text)
    test1 = []
    for i in range(len(text)):
        test1 += text[i]
    document.append(test1)


# In[151]:


result = []
for i in range(len(document)):
    vocab = []
    for w in document[i]:
        vocab.append(w)
    vocab = list(set(vocab))
    vocab.sort()
    a = []
    num = i + 1
    result.append('(대화' + str(num) + ')')
    for j in range(len(vocab)):
        t = vocab[j]
        cnt = document[i].count(t)
        a.append(t + '\t' + 'TF:' + str(cnt) + '\n')
    result.append(a)


# In[153]:


save_file_name = '2019711752_윤민형_TF'
with open('./'+save_file_name+'.txt', 'w', encoding='utf-8', newline='') as writer_text:
    vstr = ''
    for line in result:
        for a in line:
            vstr = vstr + str(a)
        # vstr = vstr.rstrip('\n') ==> rstrip
        vstr = vstr+'\n'
    
    writer_text.writelines(vstr)
    writer_text.close()
    print("[저장 완료]")


# In[ ]:




