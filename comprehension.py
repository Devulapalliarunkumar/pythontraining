#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Empty list
List = []

# Traditional approach of iterating
for character in 'python language':
	List.append(character)

# Display list
print(List)


# In[3]:


# Using list comprehension to iterate through loop
List = [character for character in 'python language']

# Displaying list
print(List)


# In[13]:


matrix = []
 
for i in range(3):
     
    # Append an empty sublist inside the list
    matrix.append([])
     
    for j in range(5):
        matrix[i].append(j)
         
print(matrix)


# In[11]:


# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)


# In[ ]:




