#!/usr/bin/env python
# coding: utf-8

# In[17]:


size=int(input())
max=0
flag=0
count=0
str=input()
arr=list(str)
for i in  range(size):
    if arr[i]==1:
        count=count+1;
        flag=1   
    elif(arr[i]==0 and flag==1):
        count=0
        flag=0
    if count>max:
            max=count
print(max)


# In[11]:


v=int(input())
w=int(input())
if w&1==1 or w<2 or w<=v:
    print("invaild")
else:
    x=((4*v)-w)//2
    print("tw",x)
    print("fw",v-x)


# In[14]:


#inorder
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def inorder(root):
    if root==None:
        return 
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("inorder traversal of a bst")
inorder(root)


# In[27]:


#preorder
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def preorder(root):
    if root==None:
        return 
    #inorder(root.lc)
    print(root.data)
    preorder(root.lc)
    preorder(root.rc)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("preorder traversal of a bst")
preorder(root)


# In[28]:


#post order
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def postorder(root):
    if root==None:
        return 
    #inorder(root.lc)
    #print(root.data)
    postorder(root.lc)
    postorder(root.rc)
    print(root.data)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("postorder traversal of a bst")
postorder(root)


# In[29]:


#vertical position...meta inheritance...
class Node:
    def __init__(self, key, l=None, r=None):
        self.key=key
        self.l=l
        self.r=r
        
def vot(node, dist, d):
    if node is None:
        return
    d.setdefault(dist,[]).append(node.key)
    vot(node.l,dist-1,d)
    vot(node.r,dist+1,d)
    
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)
        
if __name__=="__main__":
    root=Node(1)
    root.l=Node(2)
    root.r=Node(3)
    root.r.l=Node(4)
    root.r.r=Node(5)
    root.r.l.l=Node(6)
    root.r.l.r=Node(7)
    root.r.l.r.l=Node(8)
    root.r.l.r.r=Node(9)
    pvot(root)


# In[ ]:




