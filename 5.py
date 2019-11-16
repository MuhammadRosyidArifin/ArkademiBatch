#!/usr/bin/env python
# coding: utf-8

# In[12]:


def triangle(n):
    spasi = 2*n -1
    for i in range(0,n):
        for j in range(0,spasi):
            print(end=" ")
        spasi = spasi-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")


# In[13]:


baris = 5
triangle(baris)

