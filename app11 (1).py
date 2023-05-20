#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install streamlit')


# In[4]:


import streamlit as st
import pandas as pd


# In[6]:


df = pd.read_csv("C:\\Users\\kalpana\\Documents\\digital monks.csv")


# In[7]:


st.dataframe(df)


# In[ ]:




