#!/usr/bin/env python
# coding: utf-8

# In[4]:


data = [0,500,900,1600,3000,12000,43000,48000,65000,78000,98000,132000,1600324]


# In[8]:


import matplotlib.pyplot as plt
plt.plot(data)
plt.title('corona cases')
plt.xlabel('weeks')
plt.ylabel('numbers')
plt.show()
plt.xticks([1, 8, 15, 22, 28]) 


# In[ ]:




