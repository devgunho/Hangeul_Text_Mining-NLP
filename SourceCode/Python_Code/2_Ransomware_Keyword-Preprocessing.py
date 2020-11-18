#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_excel('./dataset/랜섬웨어/원문데이터_랜섬웨어.xlsx',sheet_name='Worksheet')
print(df)


# In[2]:


df=pd.read_excel('./dataset/랜섬웨어/단어빈도_랜섬웨어.xlsx',sheet_name='Worksheet')
print(df)

