#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk


# In[3]:


tk


# In[4]:


w=tk.Tk()
l1=tk.Label(w,text='welcome to SR')
e1=tk.Entry(w, show='*')
b1=tk.Button(w, text='click')
l1.pack()
e1.pack()
b1.pack()


w.mainloop()


# In[ ]:


import tkinter as tk

def sum():
    a=int(e1.get())
    
    b=int(e2.get())
    c=a+b
    e3.insert(0,str(c))

r=tk.Tk()

l1=tk.Label(r,text='Num1')
l2=tk.Label(r, text='Num2')
l3=tk.Label(r, text='Sum')

e1=tk.Entry(r)
e2=tk.Entry(r)
e3=tk.Entry(r)

b1=tk.Button(r, text=" submit", command=sum)

l1.grid(row=0,column=0, sticky=tk.W)
e1.grid(row=0, column=1, sticky=tk.E)
l2.grid(row=1,column=0, sticky=tk.W)
e2.grid(row=1, column=1, sticky=tk.E)

l3.grid(row=2, column=0, sticky=tk.W)
e3.grid(row=2, column=1, sticky=tk.E)

b1.grid(row=3, column=1, sticky=tk.W)

r.mainloop()


# In[ ]:




