#!/usr/bin/env python
# coding: utf-8

# In[1]:


#maximum of two numbers.
a=int(input())
b=int(input())
if a>b:
    print("a is maximum")
else:
    print("b is maximum ")
    


# In[2]:


#factor of a number
n=int(input())
f=int(input())
if n%f==0:
    print(f, 'is factor of' ,n)
else:
    print(f, 'is not a factor of' ,n)


# In[1]:


#maximum of 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a>b>c:
    print("a is maximum")
elif b>a>c:
    print("b is maximum")
else:
    print("c is maximum")


# In[2]:


#Category of a character enter by User
ch=input()
if (ch.isalpha()):
    print(ch, 'is alphabet')
else:
    print(ch, 'is a digit')


# In[4]:


#converting a character into Upper to Lower vis versa
ch=input()
if ch>='a' and ch<='z':
    print(ch.upper())
elif ch>='A' and ch<='Z':
    print(ch.lower())


# In[ ]:


#Determining whether the given character is vowel or not
ch=input()
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print(ch, 'is an vowel')
else:
    print('enter valid character')


# In[4]:


#To Display the corresponding day in a week by entering a number.
n=int(input())
if n==1: print("Monday")
elif n==2: print("Tuesday")
elif n==3: print("Wednesday")
elif n==4: print("Thursday")
elif n==5: print("Friday")
elif n==6: print("Saturday")
elif n==7: print("Sunday")
else: print("enter a vaild number")


# In[ ]:


#determine the character enter by the User.
ch=input()
if ch>='a' and ch<='z':
    print(ch, "lower case letter")
elif ch>='A' and ch<='Z':
    print(ch, "Upper case letter")
else:
    print(ch, "is a digit")
    


# In[2]:


#program to find the grade of a student.
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
    
    
    


# In[7]:


#finding roots of a Quadratic Equations.
a = int(input())
b = int(input())
c = int(input())
det=(b*b)-(4*a*c)
if det>=0:
    print("real roots")
    r1=(-b+(det**0.5))/2*a
    r2=(-b-(det**0.5))/2*a
    print("root1",r1)
    print("root2",r2)
elif det==0:
    print("roots are imaginary")
    r=-b/(2*a)
    print(r)
else:
    print("roots are not possible")







# In[ ]:





# In[ ]:





# In[ ]:




