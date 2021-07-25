#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import yfinance as yf


# In[ ]:


st.write("""
# Simple web app Testing
""")


# In[2]:


tickerSymbol = 'GOOGL'


# In[3]:


tickerData = yf.Ticker(tickerSymbol)


# In[5]:


tickerDf = tickerData.history(period ='id', start='2010-05-31', end='2021-05-31')


# In[7]:


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




