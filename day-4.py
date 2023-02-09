#!/usr/bin/env python
# coding: utf-8

# In[4]:


def add(a,b):
    return a+b 
a=41
b=38
operation=add
print(operation(a,b))


# In[14]:


def add(a,b):
    result =add(a+b) 
    #print(result)
a=41
b=38
print(result(a,b))
add()


# In[12]:


var1="hi"
def abc():
    global var1
    var1="goodmorning"
    print("function var1 is",var1)
abc()
print("outside function is var2 is-",var1)
var1="verygood"
print("outside fun. after modif is-",var1)


# In[24]:


#access of varibles in and out...
def out():
    var=11
    def inner():
        var=22
        print("inner varible",var)
    inner()
    print("outer variable",var)
out()
        


# In[28]:


#writing a fun. and cubation and return its model...
def cube(x):
    return (x*x*x)
num=10 #execution starts here...
result=cube(num)
print("cube",num," = ",result)


# In[36]:


#mismatch
def abc(x):
    print("hi ggfgf"+"x",x)
abc(5,5)


# In[37]:


#mismatch parameters...
def fun(i):
    print("orange",i)
j=10
fun(j)


# In[39]:


def fun(i):
    print("orange",i)
fun(4-2*4)


# In[41]:


#key arguments...
#can pass in any way...
def display(name,age,salary):
    print("name is",name)
    print("age is",age)
    print("salary",salary)
a="Arun"
b=21
c=42576
display(age=b,name=a,salary=c)


# In[43]:


#lambda function
#mulitpe parameters can accepted.
addition = lambda x,y,z:x-y+z
print("sum",addition(20,23,45))


# In[46]:


#smaller number by lambda...
def small(a,b):
    if(a<b):
        return a
    else:
        return b
add = lambda x,y:x+y
diff = lambda x,y:x-y
print("smaller of two no.",small(add(-3,-2),diff(-1,2)))


# In[47]:


#increment the values...
def increment(y):
        return (lambda x:x+1)(y)
a = 100
print("a=",a)
print("a after incrementing")
b=increment(a)
print(b)


# In[48]:


# pass a lambda fun as a fun. arg...
def fun(f,n):
       print(f(n)) #twice of 4
twice=lambda x:x*2
triple=lambda x:x*3
fun(twice ,4)
fun(triple,3)


# In[49]:


add=lambda x,y:x+y
m_and_add=lambda x,y,z:x*add(y,z)
print(m_and_add(3,4,5))


# In[52]:


x=lambda : sum(range(1,11))
print(x())


# In[56]:


#swaping of two numbers...
def fun(a,b):
        a,b=b,a
        print("after swap")
        print("a",a)
        print("b",b)
a=int(input())
b=int(input())
print("before swaping",a,b)
print("a",a)
print("b",b)
fun(a,b)


# In[61]:


#full name to 1st name is..
def fun(str1,str2):
    s=" "
    n=str1+s+str2
    return n
    print(fun("arun","devulapalli"))


# In[64]:


def eo(n):
    if(a%2==0):
        return 1
    else:
        return -1
a=int(input("enter a number"))
flag=eo(a)
if(a==1):
    print("odd")
else:
    print("even")


# In[ ]:


#calculate SI,sc->12%ROI and for for other ROI is 10%
#p=200,r=3,si=pxrxROI/100
def rate(p,r,age,R)
    ROI=R/100
    if(age>=60):
        print("senior citizen")
        si=p*r*ROI/100
        print(si)
    else:
        print("citizen")
        si=p*r*ROI/100
        print(si)
        


# In[66]:


def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))


# In[1]:


#program to find the exp(x,y) using recurrsion...
def expp(x,y):
    if(y==0):
        return 1
    else:
        return(x*expp(x,y-1))
n=int(input())
m=int(input())
print("result=",expp(n,m))


# In[8]:


#febbonacci recursive...
def feb(n):
    if(n<2):
        return 1
    return (feb(n-1)+feb(n-2)) #formula
n=int(input())
for i in range(n):
    print("Febonacci(",i,")=",feb(i))


# In[13]:


#tower of Hannoi...
def tower(n,A,B,C):
    if n>0:
        tower(n-1,A,C,B)
        if(A):
            C.append(A.pop())
        tower(n-1,B,A,C)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
tower(len(A),A,B,C)
print(A,B,C)


# In[17]:


#wildcharacters...here when astring is entered with spe.char then it checks for the String...
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n>1 and a[0]=="*" and m==0:
        return False
    if(n>1 and a[0]=="!") or (n!=0 and m!=0 and a[0]==b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0]=="*":
        return solve(a[1:],b) or solve(a,b[1:])
    return False
x=str(input("enter string with char:"))
y=str(input("enter string for match:"))
print("with wild characters:",x)
print("without wild characters:",y)
print(solve(x,y))


# In[31]:


def feb(n):
    if(n<2):
        return 1
    return (feb(n-1)+feb(n-2)) #formula
n=int(input())
for i in range(0,n-1):
    print(feb(i),end=" ")


# In[48]:


sum=0
def multi(n):
    if(n>0):
        m=str(input("enter the elements:"))
        sum=m*(m-1)
    else:
        return 0
print(sum)
n=int(input("enter the size:"))
multi(n)
#print(sum)


# In[ ]:




