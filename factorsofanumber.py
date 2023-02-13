#!/usr/bin/env python
# coding: utf-8

# In[1]:


#factors of a number
num=int(input("enter a number"))
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)

print ("Factors of {} = {}".format(num,factors))


# In[ ]:




