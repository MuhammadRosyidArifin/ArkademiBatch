#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def findPair(arr):
    checkArray = isinstance(arr,list)
    jumlah_pair = 0
    if(checkArray):
        counts = dict()
        for number in arr:
            if number in counts:
                counts[number] +=1
            else:
                counts[number] = 1
        for key in counts.keys():
            if(counts[key]>1):
                print("warna dengan kode : "+str(key)+ "\t memiliki pasangan")
                jumlah_pair +=1
            else:
                print("warna dengan kode : "+str(key)+"\t tidak memiliki pasangan")
        print("Terdapat "+ str(jumlah_pair) + " pasang kaos kaki")
    else:
        return("Bukan Array !")
    
findPair([1,5,5,10,9,13,5,1])

