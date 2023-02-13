#!/usr/bin/env python
# coding: utf-8

# In[4]:


#wapp to create a list with numbers and find out all even numbers on the screen 
l=[]
l1=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
    


# In[6]:


#wapp to combine two lists of words into single list
l=['hi','good']
a=['joy','python']
b=[]
for i in  l:
    for j in a:
        w=i+j
        b.append(w)
print(b)


# In[5]:


#wapp read list of words and store all the starting letters in another list
a=['hi','hello','python','good']
b=[]
for word in a:
    b.append(word[0])
print(b)


# In[ ]:




