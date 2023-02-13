#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROGRAMS ON SETS.
# program of union using sets.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)


# In[2]:


#program of sets to find the difference of two sets.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)


# In[6]:


#PROGRAM ON DICTIONARY
#program to print the grades of the students.
grades = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C', 'Ashley':'A'}
grades={'Ashley': 'A', 'Betty': 'B', 'Emily': 'A+', 'John': 'A', 'Mike': 'C'}

print(grades)


# In[4]:


# program to Delete set of keys from a dictionary.
sampleDict = {
  "name": "kumar",
  "age":25,
  "salary": 8000,
  "city": "warangal"
}
keysToRemove = ["name", "salary"]

sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}

print(sampleDict)


# In[7]:


#Program to find sum of all items in a Dictionary
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))


# In[ ]:




