#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=int(input("no of rows"))
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()


# In[12]:


n=int(input("no of rows"))
for i in range(n):
    for k in range(n-i):
        print(' ', end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()


# In[15]:


n=int(input())
count=0
for i in range(n):
    for j in range(i+1):
        print(count, end=' ')
        count+=1
    print()


# In[16]:


for i in range(10):
    print(i)
else:
    print("loop is completed")
    


# In[18]:


i=0
while i<=10:
    print(i)
    i=i+1
else:
    print("loop is completed")


# In[6]:


# Outer loop
for i in range(65,70):
    k=i
    # Inner loop
    for j in range(65,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


# In[ ]:




