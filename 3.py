#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def cek_kata(kalimat):
    kata = kalimat.split()
    jumlah_kata= 0;
    for word in kata:
        find_digit = re.findall("\d",word)
        if(find_digit==[]):
            jumlah_kata +=1
    print("Output \t : "+ str(jumlah_kata) + "/"+str(len(kata)))

print("input \t : ini adalah sebuah kata")
cek_kata("ini adalah sebuah kata")
print("input \t : 2 pasang sandah hilang")
cek_kata("2 pasang sandah hilang")

