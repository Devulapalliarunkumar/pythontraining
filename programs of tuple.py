#!/usr/bin/env python
# coding: utf-8

# In[1]:


#programs of Tuple.
# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)


# In[3]:


#wapp to check the membership of an item.
tup=(1,2,3,4,5,6)
print("the original tuple is:",tup)
val=4
if val in tup:
    print("value:",val, "exists in the tuple")
else:
    print("value:",val,"does not exist in the tuple")


# In[4]:


#wapp to print sum of tuple.
A = (7, 8, 9, 1, 10, 7) 
print("The original tuple is : " + str(A))
res = sum(list(A))
print("The summation of tuple elements are : " + str(res)) 


# In[5]:


#wapp to print sorted values of the tuple.
def count_digs(tup):
    return sum([len(str(ele)) for ele in tup ])
tu = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
print("The original list is : " + str(tu))
tu.sort(key = count_digs)
print("Sorted tuples : " + str(tu))


# In[6]:


#wapp to print the duplicate values
te = (1, 3, 5, 2, 3, 5, 1, 1, 3)
print("The original tuple is : " + str(te))
res = tuple(set(te))
print("The tuple after removing duplicates : " + str(res))


# In[ ]:




