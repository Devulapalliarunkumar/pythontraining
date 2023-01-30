#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi python")


# In[2]:


num=str(input())
print(int(num,17))


# In[3]:


a=10
print(a)


# In[6]:


d=4.2
print(d)


# In[8]:


far=float(input("Enter the value"))
cel=(0.58)*(far-32)
print(cel)


# In[12]:


a=int(input())
if(a >0):
    a=a+5
    print(a)
    print("positive")
else:
    print("negative")


# In[15]:


te="Telangana is a state"
if "a"in te:
    print("present")
else:
    print("absent")


# In[19]:


te="MISSISSIPPI"
te.split("S")


# In[4]:


abc='netherlands'
print(abc[1])
print(abc[1:4])


# In[6]:


abc="""netherlands australia greece"""
print(abc)


# In[7]:


abc1="hi"
abc2="hello"
abc3="hi"
print(abc1==abc2)
print(abc1==abc3)


# In[8]:


abc1="hi"
abc2="hello"
abc3="hi"
print(abc1+abc2)
print(abc1+abc3)


# In[23]:


def ls(string)
return sum(l for i in string)
string='india'
print(ls(string))


# In[27]:


N=10
a=int(input())
k=N-a
if(k<=5):
    k.update(10)
else:
    print(k)


# In[34]:


N=int(input("Enter number of candies :"))
M=int(input("Enter sold candies :"))
K=int(input("min candies :"))
p=N-M
if(K<=5):
        print("error")
else:
        #p=N-M
        print(p)


# In[1]:


s=int(input("how many digits to be entered: "))
p=int(input( ))
if(p==1):
    print(p)


# In[ ]:


size=int(input())
max=0
count=0
flag=0
str=input()
arr = list(str)
for i in range(0,size):
    if arr[i] =='1':
       count = count+1
       flag=1
    elif(arr[i]=='0' and flag==1):
        count = 0
        flag=0
    if count >max :
        max=count
        print(max)


# In[3]:


#******DAY----2*******


# In[ ]:


m=int(input())
n=int(input())
sum=0
while(m<=n):
    sum = sum +m
    m=m+1
    print("sum=", sum)


# In[ ]:




