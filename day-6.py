#!/usr/bin/env python
# coding: utf-8

# In[3]:


#oops...
#abstract...
#irs the process of handling the information by hiding...
class fruit:
    def taste(self):
        raise NotImplementedError()
        #abs lacks required derived class
        #by raising an exception
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise  NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return "Golden Yellow"
class orange(fruit):
    def taste(self):
        return "sour"
    def rich(self):
        return "vitamin C"
    def color(self):
        return "orange"
Alpanso=mango()
print(Alpanso.taste(),Alpanso.rich(),Alpanso.color())
Orange=orange()
print(Orange.taste(),Orange.rich(),Orange.color())


# In[4]:


#polymorphism... change of  anything into anotherform...
#program to interviene polymorphism on a complex numbers
class Complex():
    def __inti__(self):
        self.real=0
        self.img=0
    def setvalue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        temp=Complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=Complex()
c1.setvalue(1,2)
c2=Complex()
c2.setvalue(3,4)
c3=c1+c2
print("result is...")
c3.display()


# In[ ]:


operator --------------function name---------
+                       __add__
+=                      __iadd__

-                       __sub__
-=                      __isub__

*                       __mul__
*=                      __imul__

__truediv__()
(=, __idiv__)

**                      __pow__
**=                     __ipow__

get_ipython().run_line_magic('__mod__', '')
get_ipython().run_line_magic('=', '                     __imod__')

>>                      __rshift__
>>=                     __irshift__

<<                      __lshift__
<<=                     __ilshift

&                       __and__
&=                      __iand__

|                       __or__
|=                      __ior__

^                       __xor__
^=                      __ixor__

~                       __invert__
~=                      __iinvert__

>                       __gt__
<                       __lt__

>=                      __ge__
<=                      __le__


# In[12]:


#wapp of abstract class to dervie 2 classes
#rectangle and triangle from polygon class and
#write the methods to get their details and dimensions
#calculate the areas...
class polygon:
    def get_data(self):
            raise NotImplementedError()
    def area(self):
            raise NotImplementedError()
class rectangle(polygon):
    def get_data(self):
            self.length=float(input("length:"))
            self.breadth=float(input("breadth:"))
    def area(self):
            return self.length*self.breadth
class triangle(polygon):
    def get_data(self):
            self.base=float(input("base:"))
            self.height=float(input("height:"))
    def area(self):
            return 0.5*self.base*self.height
        
rect=rectangle()
rect.get_data()
print("area of the rectangle",rect.area())
tri=triangle()
tri.get_data()
print("area of the triangle",tri.area())


# In[18]:


# encapsulation public members...
class pub:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def Num(self):
        print("name is:",self.name)
        print("roll num is:",self.num)
obj=pub("Rony",457)
obj.Num()


# In[19]:


#program to overload the __call__method
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,o):
        return self.num*o
x=multi(10)
print(x(5))


# In[20]:


#program to over ride get item and set item methods
class mylist:
    def __init__(self,List):
        self.List=List
    def __getitem__(self,index):
        return self.List[index]
    def __setitem__(self,index,num):
        self.List[index]=num
    def __len__(self):
        return len(self.List)
    def display(self):
        print(self.List)
L=mylist([1,2,3,4,5,6,7,8,9])
print("list is......")
L.display()
index = int(input("enter the index of the list:"))
print(L[index])
index = int(input("enter the index of the list:"))
num=int(input("enter the position u want to modify"))
L[index]=num
L.display()
print("the length of list is:",len(L))


# In[24]:


#SPECIAL OR MISCELLANEOUS FUNCTIONS IN OVERLOADING
class number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self.num)
    def __oct__(self):
        return oct(self.num)
    def __setitem__(self,num):
        self.num=num
n=number(-14)
print("n is =",n.display())
print("abs(n) is =",abs(n))
n=abs(n)
print("converting to float",float(n))
print("converting to hex",hex(n))
print("converting to octa",oct(n))


# In[20]:


#inheritance flow
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print("age is",self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def displaydata(self):
        person.display(self)
        print("exp is",self.exp)
        print("research area ",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("course =",self.course)
        print("marks=",self.marks)
print("**********teacher class*****")
T=teacher("marks",43,20,"Jss")
T.displaydata()
print("*******student class*********")
S=student("kumar",20,"B.E",78)
S.displaydata()

print("T is a teacher:",isinstance(T,teacher))
print("T is a person:",isinstance(T,person))
print("T is a object:",isinstance(T,object))
print("T is a integer:",isinstance(T,int))
print("person is subclass of teacher:",issubclass(person,teacher))
print("teacher is subclass of person:",issubclass(teacher,person))


# In[7]:


#multiple inheritance...
class base1(object):
    def __init__(self):
        print("base class 1")
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base2,base1):
    pass
D=Derived()


# In[9]:


#program to call constructor of a base class from super
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D=Derived()


# In[10]:


class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class")
D=Derived()


# In[22]:


class person:   #person bc
    def name(self):
        print("name is kumar ")
class teacher(person):   #cclass derived from person
    def qual(self):
        print('qualification is phd')
class hod(teacher):   #class derived from teacher 
    def expe(self):
        print("experience is 22 years old")
HOD=hod()
HOD.name()
HOD.qual()
HOD.expe()


# In[25]:


#multi path inheritance
class student:
    def name(self):
        print("name is kumar")
class academic(student):
    def acad_score(self):
        print("academic score 90% above")
class EEE(student):
    def EEE_score(self):
        print("EEE score -----60% and above")
class result(academic,EEE):
    def eligibility(self):
        print("********eligibility to apply*******")
        self.acad_score()
        self.EEE_score()
R=result()
R.eligibility()


# In[ ]:




