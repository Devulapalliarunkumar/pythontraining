#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input())
while(num!=0):
    temp = num%10
    print(temp, end=" ")
    num=num//10


# In[3]:


n=int(input())
avg = 0.0
s=0
for i in range(1,n+1):
    s = s+i
avg=s/i
print("sum=", s)
print("avg=", avg)


# In[6]:


n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    


# In[ ]:


for i in range(1900,2101):
    if i%4==0:
        print(i, end=" ")


# In[2]:


n=int(input())
s=0.0
for i in range(1,n+1):
    a=1.0/i
    s=s+a
print("the sum of 1,1/2,...1/"+str(n)+"is"+str(s))


# In[5]:


n=int(input())
s=0.0
for i in range(1,n+1):
    a=1.0/i**2
    s=s+a
print("the sum of 1,1/2^2,...1/^2"+str(n)+"is"+str(s))


# In[2]:


n=int(input())
s=0.0
for i in range(1,n+1):
    a=1.0/i**3
    s=s+a
print("the sum of 1,1/2^3,...1/^3"+str(n)+"is"+str(s))


# In[5]:


str = "hello"
print(str.center(10,'$'))


# In[8]:


str="hi"
substr="hehellohi"
print(substr.count(str,0,len(substr)))


# In[9]:


str="he is a tall"
print(str.find("tall",0,len(str)))


# In[10]:


#left justifiation->ljust(width[,fillchar])
str="hi"
print(str.ljust(20,"^")) #rjust


# In[15]:


#zfill(width)
str="7"
print(str.zfill(4)) 


# In[17]:


ord('A')


# In[18]:


ord('Z')


# In[19]:


str='hi asdef'
print(max(str))


# In[24]:


str="morning moon"
print(str.title())
print(str.swapcase())
print(str.title().swapcase())


# In[28]:


str="morning moon"
print(list(enumerate(str)))


# In[31]:


str="India has won"
for i in range(0,len(str)):
    print(str[i],end=" ")


# In[32]:


str="india has won"
for i in str:
    print(i,end=" ")


# In[36]:


#caeser cipher
str="India is in danger"
index=0
while index<len(str):
    letter = str[index]
    print(chr(ord(letter)+1),end=" ")
    index +=1


# In[38]:


ord('l')


# In[44]:


#abecedarian series
str="ate"
list=['A','B','C','D','E']
for i in list:
    print(i+str)


# In[48]:


#series
val=int(input())
a=b=0
for i in range(1,val+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
    if (val%2!=0):
        print('{} at accordance {}'.format(val, a-7))
    else:
        print('{} at accordance {}'.format(val, b-6))


# In[72]:


val=int(input())
a=1
b=1
for i in range(3,val+1):
    if(i%2==0):
        a=a*3
    else:
        b=b*2
if(val%2==0):
    print(a)
else:
    print(b)


# In[66]:


num=int(input())
a,b=1,1
for i in range(3,num+1):
    if i%2==0:
        a=a*3 #even
    else:
        b=b*2 #odd
if(num%2==0):
    print(a)
else:
    print(b)
    


# In[ ]:


N=int(input("enter number of days:"))
M=int(input("enter number of Obligations:"))
K=int(input("enter how many obligations can be cancelled:"))
arr = [0]*n
for i in range(M):
    arr[i]=int(input())
ans=0
arr.sort()
if k>0:
    for i in range(k+1,m+3,1)
        ans=max(ans,arr[i]-arr[i-k-1]-1)
else:
    j=0
    while arr[j]==0:
        j=j+1
    count =0
    for i in range(1,n-1,1)
    


# In[3]:


list1=[10,14,15,17]
print(*list1)


# In[ ]:




