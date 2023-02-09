#!/usr/bin/env python
# coding: utf-8

# In[7]:


#greatest of 3 numbers...
x=int(input("enter a value for x:"))
y=int(input("enter a value for y:"))
z=int(input("enter a value for z:"))
if x>y and x>z:
    print("X is greater",x)
elif y>x and y>z:
    print("y is greater",y)
else:
    print("z is greater",z)


# In[31]:


#pattern
n=int(input("enter the rows"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


# In[32]:


n=int(input("enter the rows"))
for i in range(n):
    for j in range(i+1):
        print('*',end=" ") #"*"
    print("\n")


# In[33]:


#factorial of a number...

#def fact(n):
#    if(n==0):
#        return 1
 #   return fact(n-1)*n

#n=int(input())
#p=fact(n)
#print(p)

num=int(input())
sum=1
for i in range(1,num+1):
    sum=sum*i
print(sum)


# In[30]:


#fibonacci series...
def feb(n):
    if(n<2):
        return 1
    return (feb(n-1)+feb(n-2)) #formula
n=int(input())
for i in range(n):
    print("Febonacci(",i,")=",feb(i))


# In[96]:


#prime or not...
n=int(input())
if(n==0 or n==1):
    print("not a prime")
elif(n%2==1):
    print("it is prime")
else:
    print("not a prime")


# In[87]:


#pp to remove an empty tuple(s) from a list of tuples...
tuple1=[('a','b','c'),('v','e','t'),()]
l=[]
for i in range(tuple1):
    t=0
    


# In[89]:


#To calculate the average of elements in a list...
e_list=['1','2','5','4','8']
#l=[]
#for i in range(e_list):
  #  ele=int(input())
   # l.append(e_list)
    
pmp=sum(e_list)
print(pmp)


# In[60]:


#after removing the 0th,4th,5th
list2=['Red','Green','White','Black','Pink','Yellow']

list2.remove(list2[0])
list2.remove(list2[4])
list2.remove(list2[3])
print(list2)


# In[79]:


#pp to generate the all permutations of a python...
n=int(input("enter the size of string:"))
m=[]
for i in range(n):
    ele=int(input())
    m.append(ele)
    
for j in range(len(l)):
    print(l[i],l[j])
    print(l[j],l[i])


# In[76]:


#pp to calculate the product,multiplying all the numbers of a given tuple...
n=int(input("enter the size of tuple:"))
m=[]
for i in range(n):
    ele=int(input())
    m.append(ele)
    
t=tuple(m)
print(sum[t])
mul=m
for i in range(n):
    mul=m*t(i)
print(mul)


# In[93]:


from itertools import permutations
l=['p','y','t','h','o','n']
p=permutations(l)
for i in p:
    for j in i:
        print(j,end=" ")
    print()


# In[98]:


#counting repeated characters in a string...

str="a"
substr="arun kumar"
print(substr.count(str,0,len(substr)))


# In[101]:


#Reverse a string if it's length is a multiple of 4...
str=input("enter  a string:")
num=
for i in range(str):
    if(i==4,8,12,16,20):
        mt=reverse(str)
        print(mt)
#substr="arun kumar"

#print(str.count(len(str)))


# In[ ]:


#TO separate even ,odd and zeros from alist...


# In[ ]:


#split a given dictionary of lists into list of dictionaries...

