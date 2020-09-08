#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats as st
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('C:/Users/admin/Desktop/houseprices-1.csv')


# In[3]:


data


# In[7]:


price = data.Price
area = data.LivingArea
age = data.Age
size = data.LotSize


# In[9]:


st.probplot(price, plot = plt)
plt.show()


# In[6]:


st.mstats.normaltest(price)


# In[11]:


st.probplot(age, plot = plt)
plt.show()


# In[12]:


st.mstats.normaltest(age)


# In[13]:


st.probplot(size, plot = plt)
plt.show()


# In[15]:


st.mstats.normaltest(size)


# In[17]:


st.probplot(area, plot = plt)
plt.show()


# In[18]:


st.mstats.normaltest(area)

