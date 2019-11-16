#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


def usernameValidation(username):
    x = len(username)
    if x == 7 :
        regex = re.findall("[A-Z]",username)
        if len(regex) == x:
            return True
        else:
            return False
    else :
        return False


# In[3]:


def passwordValidation(password):
    if len(password)==7:
        try:
            x = int(password[0:3])
            angka = password[0:3]
            reg = re.findall(angka[0],angka)
            if(len(reg)==3):
                if(password[3]=="*"):
                    text = password[4:7]
                    reg2 = re.findall(text[0],text)
                    if(len(reg2)==3):
                        return True
                else:
                    return False
            else:
                return False
        except ValueError:
            return False
    else:
        return False


# In[4]:


user1 = usernameValidation("ARKDEMY")
user2 = usernameValidation("GALIH")
pass1 = passwordValidation("111*sss")
pass2 = passwordValidation("1234*try")
print("username(ARKDEMY)")
print(user1)
print("username(GALIH)")
print(user2)
print("password(111*sss)")
print(pass1)
print("password(1234*try)")
print(pass2)

