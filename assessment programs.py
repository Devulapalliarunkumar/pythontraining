#!/usr/bin/env python
# coding: utf-8

# In[16]:


n=int(input())
PreviousNum = 0
for i in range (0,n):
    if(i==0):
        PreviousNum=0
    else:
        PreviousNum=i-1
    sum = PreviousNum + i
    print('Current Number',i,'Previous Number',+PreviousNum,'Sum:', PreviousNum+i)


# In[ ]:




