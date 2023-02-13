#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Programs on list
#wapp to print n numbers.
l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
print('all the elements',l)


# In[3]:


#wapp to print n numbers.
l=[] 
n=int(input()) 
for i in range(n): 
    x=int(input()) 
    l.append(x) 
print('all the elements',l)


# In[1]:


#wapp to combine the two lists and printing as a list.
l=['hi','good']
l1=['joy','python']
l2=[]
for i in l:
    for j in l1:
        w=i+j
        l2.append(w)
print(l2)


# In[2]:


#wapp to print the beginning letters of a list.
l=['hi','hello','python','program']
l1=[]
for word in l:
    l1.append(word[0])
print(l1)


# In[4]:


#wapp to print the n numbers and display them on screen ,find the even numbers on the from displayed.
l=[]
l1=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
print('all the elements',l)
for i in l:
    if i%2==0:
        l1.append(i)
print(l1)


# In[12]:


#wapp to print the duplicate values in the list.
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


# In[ ]:




