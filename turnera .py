#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


college = pd.read_csv('recent-grads.csv')


# In[14]:


college.head()


# In[15]:


college.info()


# In[16]:


college.describe()

# draw line graph between college rank and Full Time, Part Time and Unemployment Rate
# In[17]:


college.plot(x="Rank",y=["Part_time"])
plt.show()


# In[18]:


college.plot(x="Rank",y=["Full_time"])
plt.show()


# In[26]:


college.plot(x="Rank",y=["Unemployment_rate"])
plt.show()


# In[20]:


college.plot(x="Rank",y=["Part_time","Full_time","Unemployment_rate"])
plt.show()


# In[ ]:





# In[ ]:





# bar graph between college rank and College jobs and Non College jobs

# In[ ]:





# In[28]:


college.plot(x="Rank", y=["College_jobs"], kind="bar")


# In[29]:


college.plot(x="Rank", y=["Non_college_jobs"], kind="bar")


# In[30]:


college.plot(x="Rank", y=["College_jobs","Non_college_jobs"], kind="bar")


# In[ ]:




