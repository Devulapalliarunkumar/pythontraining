#!/usr/bin/env python
# coding: utf-8

# In[6]:


#pp to add two numbers using functions.

def add(a, b):
    c=a+b
    a=a+1
    print(c)
    print(a)
x=int(input())
y=int(input())
add(x,y)
print(x,y)


# In[9]:


#pp to compare two numbers
#no argument and no return type

def compare():
    a=int(input())
    b=int(input())
    if a==b:
        print("both are equal")
    else:
        print("not equal")
compare() #function calling


# In[25]:


#pp to compare two numbers
#no argument and with return type

def comapare():
    a=int(input())
    b=int(input())
    if a==b:
        return 1
    else:
        return 0
res=compare(a,b)
if res==1:
        print("both are equal")
else:
        print("not equal")


# In[1]:


#with argument and no return type

def compare(a,b):
    if a==b:
        print("both are equal")
    else:
        print("not equal")
a=int(input())
b=int(input())
    
compare(a,b)


# In[22]:


#with argument and with return type

def compare(a,b):
    a=int(input())
    b=int(input())
    if a==b:
        return 1
    else:
        return 0
res=compare(a,b)
if res==1:
    print("both are equal")
else:
    print("not equal")


# In[ ]:




