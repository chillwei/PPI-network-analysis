#!/usr/bin/env python
# coding: utf-8

# This python file is used to filter out the self interaction data and rewrite it in new 

# In[12]:


import pandas as pd
import os
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
import networkx as nx


# In[13]:


# import data
data = os.path.join('BIOGRID-ORGANISM-Homo_sapiens-4.4.205.tab3.txt')


# In[14]:


df = pd.read_csv(data,delimiter="\t")


# In[15]:


# simplify the dataframe by only showing the data we are going to use later for network analysis
df2 = df[['Official Symbol Interactor A','Official Symbol Interactor B','Throughput','Experimental System Type','Experimental System','Publication Source']]


# In[16]:


# all physical interaction
physical_df = df2.loc[df['Experimental System Type'] == 'physical']
#physical_df.head()


# In[17]:


# separate different network as required
# low throughput
low_df = physical_df.loc[df['Throughput'] == 'Low Throughput']
#low_df.head()


# In[18]:


# high throughput
high_df = physical_df.loc[df['Throughput'] == 'High Throughput']
#high_df.head()


# In[ ]:


# save all the data frame as csv
physical_df.to_csv('physical_df.csv',index= False)
low_df.to_csv('low_df.csv',index= False)
high_df.to_csv('high_df.csv',index= False)


# In[7]:


# path
#high_data = os.path.join('high_df.csv')
#low_data = os.path.join('low_df.csv')
#physical_data = os.path.join('physical_df.csv') 


# In[11]:


#high_df = pd.read_csv(high_data)
#low_df = pd.read_csv(low_data)
#physical_df = pd.read_csv(physical_data)


# In[10]:


# not considering self-loop
# filter the self interaction data
def filter_self_loop(df):
    df2 = df.copy()
    for idx, row in df.iterrows():
        InteractorA = row['Official Symbol Interactor A']
        InteractorB = row['Official Symbol Interactor B']
        if InteractorA == InteractorB:
            print('Found self-loop')
            print(idx)
            df2 = df2.drop(idx)
    return df2
        


# In[ ]:


high_filter  = filter_self_loop(high_df)


# In[ ]:


high_filter.to_csv('high_self_loop_filter_data.csv',index= False)


# In[ ]:


low_filter  = filter_self_loop(low_df)


# In[ ]:


low_filter.to_csv('low_self_loop_filter_data.csv',index= False)


# In[ ]:


physical_filter  = filter_self_loop(physical_df)


# In[ ]:


physical_filter.to_csv('physical_self_loop_filter_data.csv',index= False)

