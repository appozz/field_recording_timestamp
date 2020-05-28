#!/usr/bin/env python
# coding: utf-8

# In[41]:


import os, datetime


# In[ ]:





# In[42]:


datetime.datetime.fromtimestamp(float(os.path.getmtime("ZOOM0035_Tr1.WAV"))).strftime("%Y%m%d")


# In[43]:


# I have found the year, month, day but I also want the time


# In[45]:


datetime.datetime.fromtimestamp(float(os.path.getmtime("ZOOM0035_Tr1.WAV"))).strftime("%Y%m%d")


# In[46]:


datetime.datetime.fromtimestamp(float(os.path.getmtime("ZOOM0035_Tr1.WAV"))).strftime("%Y%m%dT%H:%M")


# In[47]:


#OK THAT WORKS, I FOUND THE TIMESTAMP NOW I HAVE TO FIND A WAY TO RENAME THE FILE USING THE TIMESTAMP


# In[48]:


timestamp = datetime.datetime.fromtimestamp(float(os.path.getmtime("ZOOM0035_Tr1.WAV"))).strftime("%Y%m%dT%H:%M")
src = "ZOOM0035_Tr1.WAV" 
dst = timestamp + "ch1.WAV"

os.rename(src, dst)


# In[49]:


dst


# In[50]:


#OK I DID IT
#ONE PROBLEM IS THAT THE TIMESTAMP IS REALLY JUST THE TIME I UPLOADED THE FILE TO THE NOTEBOOK
#I NEED THE ORIGINAL TIMESTAMP FROM WHEN THE FILE WAS RECORDED ON THE RECORDER


# In[ ]:




