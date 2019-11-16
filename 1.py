#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
def isiBiodata(nama, umur):
    objekBiodata = {'name': nama,'age' : umur,'address':'Bandung','hobbies': ['game','riding'],'is_married': False,'list_school': {'name':'sangga buana','year_in':2015,'year_on':2019,'major':'teknik informatika'},'skills':{'ngoding': 'beginner','problem_solved': 'advance'},'interest_in_coding':True}
    jsonBiodata = json.dumps(objekBiodata)
    return jsonBiodata


# In[5]:


result = isiBiodata('muhammad rosyid arifin',23)
print(result)


# In[ ]:




