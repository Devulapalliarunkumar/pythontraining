#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Student:
    name="Random Name"
    __rollnumber=100     #__ used for private variable
    def get_rollnumber(self):
        return self.__rollnumber
    def set_rollnumber(self,new_value):
        self.__rollnumber=new_value
obj=Student()
print(obj.name)
print(obj.rollnumber)


# In[3]:


class A:
    def method_1(self):
        print("in class A")
class B:
    def method_1(self):
        print("CLASS b")
class Child(A,B):
    pass
obj=Child()


# In[30]:


#dictionary program to read and store user name ,password...
a=int(input("enter the size:"))
arr=[]
for i in range(a):
    str1=input()
    M=int(input())
    arr.append({str1:M})
print(arr)
U1=(input("user:"))
p1=int(input("pw:"))
found=False
for obj in arr:
    try:
        M=obj[U1]
        found=True
        if p1==M:
            print("vaild")
        else:
            print("invaild")
    except:
        pass
if found==False:
    print("invaild user")
    


# In[31]:


#task-2
a=int(input("enter the size:"))
arr=[]
for i in range(a):
    str1=input()
    M=int(input())
    arr.append({str1:M})
print(arr)
A=(input("check username:"))
B=int(input("check password:"))
if(A in arr):
    print("vaild")
else:
    print("Invaild")
if(B in arr):
    print("vaild")
else:
    print("Invaild")
#print(arr)


# In[21]:


#stacks...
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop(0)
print(stack)


# In[26]:


#queues.....
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)
queue.()
print(queue)


# In[27]:


#r,p,s....
from random import randint
#print(random.randint(0,25))
choice=['rock','paper','scissor']
player=input((f"choose from {choice} ")).lower()
comp=choice[randint(0,2)]
print("computer chooses:",comp)
if(player==comp):
    print("draw match")
elif(player=='paper' and comp=="rock"):
    print("player win")
elif(player=='rock' and comp=="scissor"):
    print("player win")
elif(player=='scissor' and comp=="paper"):
    print("player win")
else:
    print("computer win")


# In[29]:


#r,p,s....
from random import randint
#print(random.randint(0,25))

choice=['rock','paper','scissor']
limit=3
ps=0
cs=0
while True:
    player=input((f"choose from {choice} ")).lower()
    comp=choice[randint(0,2)]
    print("computer chooses:",comp)
    if(player==comp):
        print("draw match")
    elif(player=='paper' and comp=="rock"):
        print("player win")
        ps+=1
    elif(player=='rock' and comp=="scissor"):
        print("player win")
        ps+=1
    elif(player=='scissor' and comp=="paper"):
        print("player win")
        ps+=1
    else:
        print("computer win")
        cs+=1
    if ps==limit or cs==limit:
        break
if ps>cs:
    print("player wins")
else:
    print("computer wins")


# In[ ]:





# In[ ]:




