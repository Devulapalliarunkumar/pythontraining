#!/usr/bin/env python
# coding: utf-8

# In[1]:


str1='ABCDEFGH'
str2="ate"
for letter in str1:
    print(letter +str2, end=" ")


# In[5]:


n=int(input("enter the rows"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ") #"*"
    print("\n")


# In[10]:


n=int(input("enter the rows"))
for i in range(n,0,-1):
    for j in range(0,i):
        print(j+1,end=" ") #"*"
    print("\n")


# In[19]:


n=int(input("enter the rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("@",end=" ")
        #print(j,end=" ") #"*"
    print()


# In[27]:


n=int(input("enter the rows:"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print(" ", end=" ")
        else:
            print("@", end=" ")
        j=j+1
    i=i+1
    print()


# In[15]:


n=int(input("enter the rows:"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print("", end=" ")
        else:
            print("@", end=" ")
        j=j+1
    i=i+1
    print()


# In[22]:


#rhombus
n=int(input())
i=1
while(i<=n):
    j=n
    while(j>i):
        print(" ",end=" ")
        j-=1
    print('*',end=" ")
    k=1
    while(k<2*(i-1)):
        print(" ",end=" ")
        k+=1
    if(i==1):
        print()
    else:
        print("*")
    i+=1
i=n-1
while(i>=1):
    j=n
    while(j>i):
        print(" ",end=" ")
        j-=1
    print("*",end=" ")
    k=1
    while k<2*(i-1):
        print(" ",end=" ")
        k+=1
    if(i==1):
        print()
    else:
        print("*")
    i-=1


# In[30]:


rows=7
k=2*rows-2
for i in range(0, rows):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0, i+1):
        print("*",end=" ")
    print("")


# In[3]:


n=int(input("enter the rows"))
for i in range(n):
    for j in range(i+1):
        print("@",end=" ") #"*"
    print("\n")
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print("", end=" ")
        else:
            print("@", end=" ")
        j=j+1
    i=i+1
    print()


# In[29]:


word="California"
x=""
for i in word:
    x+=i
    print(x)


# In[4]:


a=65
r=11
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")


# In[32]:


a=65
r=5
m=(2*a)-2
for i in range(0,r):
    for j in range(0,m):
        print(end=" ")
    m=m-1    
    for j in range(0, i+1):
        ch=chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")


# In[22]:


n=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


# In[28]:


def diff(a,b):
    return a-b
x=20
y=10
operation = diff
print(operation(x,y))


# In[29]:


def fun():
    for i in range(5):
        print("hi..........!")
fun()


# In[30]:


def diff(a,b):
    result = a-b
    print("difference of a&b is",result)
x=20
y=10
diff(x,y)


# In[43]:


#two inputs and print prime numbers b/w them...
#2nd must be greater than 1st for,while...
n=int(input())
m=int(input())
if(n<=0 or m<=0 or n>m):
    print("Provide valid input....")
else:
    while(n<=m):
        if n==2:
            print(n,end=" ")
        elif(n==1):
            n+=1
            continue
        else:
            flag=0
            for i in range(2,n//2+1):
                if(n%i==0):
                    flag=1
                    break
            if flag==0:
                print(n,end=" ")
        n+=1


# In[53]:


rows=5
k=rows+2
for i in range(0, rows):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
'''k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0, i+1):
        print("*",end=" ")
    print("")
    '''


# In[63]:


n=int(input("enter the rows"))
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==n or j==n:
            print("*",end=" ") #"*"
        else:
            print(" ",end=" ")
    print()


# In[67]:


n=int(input("enter the rows"))
val=n*2-1
for i in range(1,val+1):
    for j in range(1,val+1):
            if i==j or j==val-i+1:
                print("*",end=" ") #"*"
            else:
                print(" ",end=" ")
    print()


# In[69]:


rows=5
k=2*rows-2
for i in range(0, rows):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
'''k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0, i+1):
        print("*",end=" ")
    print("")'''
    
n=int(input("enter the rows:"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print("", end=" ")
        else:
            print("*", end=" ")
        j=j+1
    i=i+1
    print()


# In[85]:


n=5
k=2*n-2
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print("", end=" ")
        else:
            print("*", end=" ")
        j=j+1
    i=i+1
    print()
for i in range(0,n):
    for j in range(0,k):
            print(end=' ')
            k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
    print()


# In[87]:


n=int(input())
val=0
st=int(n/2+1)
if(n%2!=0):
    for i in range(1,int(n/2+2)):
        for j in range(1,val+1):
            print(" ",end=" ")
        for k in range(1,st+1):
            print("*",end=" ")
        print()
        val+=1
        st-=1
    val-=2
    st+=2
    for i in range(int(n/2+2),n+1):
        for j in range(1,val+1):
            print(" ",end=" ")
        for k in range(1,st+1):
            print("*",end=" ")
        print()
        val-=1
        st+=1
else:
    print("provide accurate input")


# In[ ]:




