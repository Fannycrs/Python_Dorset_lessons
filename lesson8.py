# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:17:19 2023

@author: fanny
"""

#dictionnary: nomdico = {"":"","":""}
#dico[key]=value  pour ajouter la value
#del dico[key]
#dico.pop()  remove the item with the specifi key
#dico.clear() remove all,    update() add or change dico item, copy() return a copy of the dico, 
#popitem()   remove the last one, values() return all dico values  / keys()  return all keys
#get( return the value of the specific key

Dict = dict({1:"one",2:"two"})
print (Dict)


my_list={1 :"Hello","Hi":25, "Howdy":100}
print(1 in my_list)
print("Howdy" not in my_list)
print("Hello" in my_list)

for ele in my_list:
    print (ele)
"""
for keys,values in my_list.items():
    print(keys)
    print(values)

cities =('Paris','Athenes')

continent='Europe'

my_dico=dict.fromkeys(cities,continent)

print (my_dico)

keys=['Ten','Twenty','Thirty']
values=[10,20,30]
dicti=dict(zip(keys,values))
print(dicti)

dic2 = {'Fourty':40, 'Fifty':50}

dicti.update(dic2)





sampleDict ={
    "class": {
        "student": {
            "name":"Mike",
            "marks":{
                "physics" :70,
                "history" :80
                }
            }
        }  
}


sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
    }
keys=["name","salary"]

sample_dict.pop("name")
sample_dict.pop("salary")

print(sample_dict)


dic4={'emp1':{'name':'John','salary':7500},
      'emp2':{'name':'Emma','salary':8000},
      'emp3':{'name':'Brad','salary':500}
      }

dic4['emp3']['salary']=8500


"""

import numpy as np
vect=np.linspace(10, 30, 20,dtype='int32')
vect[4]=1
print(vect)


numpy.arange








