#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program to access a class var using a class object
class abc:
    var=22
obj = abc()
print(obj.var)


# In[23]:


#program to access a class member using class obj
class abc:
    var=22
    def display(self):
        print("this is calls method")
obj=abc()
print(obj.var)
obj.display()
print(obj.var) #abc()


# In[3]:


# __init__--------------constructor method
#program to illustrate the constructor
class abc:
    def __init__(self,val):
        print("in class method")
        self.val=val
        print("the value is:",val)
obj=abc(10)


# In[4]:


#program to differentiate between class and obj variable
class abc():
    class_var = 0 # it is class variable
    def __init__(self,var):
        abc.class_var+=1
        self.var=var   # it is obj variable
        print("THe object variable is :",var)
        print("The class value of c-=var",abc.class_var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)


# In[24]:


#program illustrating a modification on numerics
class Number:
    even=0  #default value
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.even_odd(20)


# In[25]:


class eveodd:
    l1=[]
    l2=[]
    def check(self,num):
            self.num=num
            if num%2==0:
                Number.l1.append(num)
            else:
                Number.l2.append(num)
n1=Number()
#n1.Number()
#n2=Number()
#n3=Number()
#n4=Number()
n1.check(21)
print("The even numbers are:",Number.l1)
print("The odd numbers are:",Number.l2)


# In[7]:


class Number:
    even=[]
    odd=[]
    def _init_(self,num):
        self.num=num
        if num%2== 0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1=Number(21)
n2=Number(76)
n3=Number(91)
n4=Number(84)
n5=Number(56)
print("Evens are__:",Number.even)
print("Odd are__:",Number.odd)


# In[8]:


class Number:
    even=[]
    odd=[]
    def _init_(self,num):
        self.num=num
        if num%2== 0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1=Number(21)
n2=Number(76)
n3=Number(91)
n4=Number(84)
n5=Number(56)
print("Evens are__:",Number.even)
print("Odd are__:",Number.odd)


# In[9]:


#delete method -------------c++ java analogus to destructors
#general syntax  __del__
class abc():
    class_var = 0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the object value is",var)
        print("the class value",abc.class_var)
    def __del__(self):
        abc.class_var -= 1
        print("object with value %d is going out of scope",self.var)
obj1 = abc(11)
obj2 = abc(22)
obj3 = abc(33)
del obj1
del obj2
del obj3


# In[10]:


# program to demonstrate get and set items in a list
class numbers:
    def __init__(self,mylist):
        self.mylist = mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index] = val
numlist = numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])


# In[11]:



class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
obj = ABC("abcdef",10)
print("the value stored in obj is",repr(obj))
print("The length of the name stored in obj",len(obj))
obj1 = ABC("ghijkl",1)
val = obj.__cmp__(obj1)
if val==0:
    print("both values are equal")
elif val==-1:
    print("1st value is less thaan second")
else:
    print("2nd value is less than 1st")


# In[12]:


# is for illustrating use of a private method
class abc():
    def __init__(self,var):
        self.__var = var
    def __display(self):
        print("This from class method var = ",self.__var)
obj=abc(10)
obj._abc__display()


# In[13]:


# to call a class method from another method of same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj = abc(10)
obj.add_2()


# In[14]:


# program to show how a class method calls a function
# which is defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
    def modify(self):
        self.var = scale_10(self.var)
obj = abc(10)
obj.display()
obj.modify()
obj.display()


# In[ ]:


#built-in attributes
#for get set and delete
1. hasattr(obj,name)-----checks obj possesses the attributes values or not
2. getattr(obj,name[,default])
3. set attr(obj,name,value) ----which is used to set an attribute of the object
4. delattr(obj,name)---------permanent deletion ,


# In[15]:


# proram to demo builtin
class abc():
    def __init__(self,var):
        self.var = var
    def display(self):
        print("var is ",self.var)
obj = abc(10)
obj.display()
print("check whether obj has attribute var ?")
getattr(obj,'var')
setattr(obj, 'count',50)
print("after setting value,var is",obj.var)
setattr(obj,'count',10)
print("new variable count is created and its val=",obj.count)
delattr(obj,'var')
setattr(obj, 'count',50)
print("after deleting the attr, var is:",obj.count)


# In[ ]:


#built-in class attributes

#.dict
#.doc
#.name
#.bases
class abc():
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
    def display(self):
        print("var1 is =",self.var1)
        print("var2 is =",self.var2)
obj = abc(10,12.34)
obj.display()
print("object.__dict__ -",obj.__dict__)
print("object.__doc__ -",obj.__doc__)
print("object.__name__ -",abc.__name__)
print("object.__module__ -",obj.__module__)
print("object.__basdes__ -",abc.__bases__)


# In[16]:


# garbage program
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l)
start=0

end=len(l)
step=int(input())
for i in range(start,end,step):
    x=i
    print(l[x:x+step])


# In[17]:


l=[]
ele=int(input())
l.append(ele)
print(l)
start=0
end=len(l)
start,end=end,start
print(l)


# In[18]:


def fibo(n):
    if n<2:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
#n=int(input())
for i in range(0,9):
    print(fibo(i),end=" ")


# In[19]:


n=int(input())
m=int(input())
count=0
for i in range(n,m+1):
    if i%7==0 and i%5==0:
        count=count+1
print(count)


# In[ ]:




