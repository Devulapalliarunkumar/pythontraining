#!/usr/bin/env python
# coding: utf-8

# In[2]:


#program to calculate the average of first n natural numbers.
num = int(input('How many numbers: '))
total_sum = 0
 
for n in range(num):
    numbers = int(input('Enter number : '))
    total_sum += numbers
 
    avg=total_sum/num
print('Average of ', num, ' numbers is :', avg)


# In[4]:


#python program to find squares of all numbers present in a list.
numbers = [1, 2, 3, 4, 5]

def square(number):
return number ** 2

squaring_iterator = map(square, numbers)
squared_numbers = list(squaring_iterator)

print(squared_numbers)


# In[14]:


#multiplication table.
num = 7

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
  print(num, 'x', i, '=', num*i)


# In[8]:


# Python program to find the factorial of a number provided by the user.
num =int(input())

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[2]:


#program to classify the given number is prime or composite.
num = int(input())
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is a composite")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[4]:


#program to print series 1+1/2+1/3+....1/n
i = 1
s = 0.0
for i in range(1, i+1):
    s = 1/i
    print('s')
    


# In[ ]:





# In[ ]:




