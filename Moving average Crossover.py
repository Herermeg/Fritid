#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/assignment2-machinelearning/TSLA.csv", sep=',')


# In[3]:


df


# In[4]:


df['MA20'] = df['Adj Close'].rolling(20).mean()
df['MA60'] = df['Adj Close'].rolling(60).mean()


# In[5]:


df


# In[6]:


df = df.dropna()


# In[7]:


df = df[['Adj Close','MA20','MA60']]


# In[8]:


df


# In[9]:


Buy = []
Sell = []

for i in range(len(df)):
    if df.MA20.iloc[i] > df.MA60.iloc[i]     and df.MA20.iloc[i-1] < df.MA60.iloc[i-1]:
        Buy.append(i)
    elif df.MA20.iloc[i] < df.MA60.iloc[i]     and df.MA20.iloc[i-1] > df.MA60.iloc[i-1]:
        Sell.append(i)


# In[10]:


Buy


# In[11]:


Sell


# In[12]:


plt.figure(figsize =(30,15))
plt.plot(df['Adj Close'], label = 'Asset price', c = 'blue')
plt.plot(df['MA20'], label='MA20', c='k')
plt.plot(df['MA60'], label='MA60', c='magenta')
plt.scatter(df.iloc[Buy].index,df.iloc[Buy]['Adj Close'], marker='^', color='g', s=100)
plt.scatter(df.iloc[Sell].index,df.iloc[Sell]['Adj Close'], marker='v', color='r', s=100)
plt.legend()
plt.show()


# In[ ]:




