#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to Extract Unique values dictionary values?

# In[1]:


#ans:-
dict1 = {'a' : [3, 64, 17, 66],
             'b' : [1, 21, 47, 45],
             'c' : [0, 17, 7, 81],
             'd' : [3, 3, 4,8]}

un_val = set([ele for val in dict1.values() for ele in val])
print("unique values are: {}".format(un_val))


# 2.	Write a Python program to find the sum of all items in a dictionary?

# In[2]:


#ans:=

dict2 = {'a' : 22,
             'b' :  21,
             'c' : 52,
             'd' : 56}

sum = 0
for i in dict2.values():
    sum +=sum + i
print("Sun of all items: {}".format(sum))
     


# 3.	Write a Python program to Merging two Dictionaries?

# In[3]:


#ans:-
one = { 'x': 2, 'y': 3}
two = { 'y': 5, 'z': 6}
both = one.copy()
both.update(two)
print("dict a : ", one)
print("Dict b : ", two)
print('updated dictionary : {}'.format(both))


# 4.	Write a Python program to convert key-values list to flat dictionary?

# In[4]:


#ans:=
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))
  
# printing result 
print("Flattened dictionary : " + str(res))


# 5.	Write a Python program to insertion at the beginning in OrderedDict?

# In[10]:


#ans:=
from collections import OrderedDict 
  
def checkOrderofString(str, pattern): 
      
    # create empty OrderedDict 
    dict = OrderedDict.fromkeys(str) 
    print(dict)   
    ptrlen = 0
    for key,value in dict.items(): 
        
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete pattern string 
        if (ptrlen == (len(pattern))):            
            return 'true'
  
    # if we come out from for loop that means order was mismatched 
    return 'false'
  

string = input("enter string : ")
pattern = input("Enter Pattern : ")
if checkOrderofString(string,pattern):
    print("Pattern matched")
else:
    print("Pattern not matched")


# 6.Write a Python program to sort Python Dictionaries by Key or Value?

# In[11]:


#ans:-
dict= {4:5 ,7:8 ,4:3 ,6:9 ,9:5 ,4:2 }
#Print sorted list of keys
print(sorted(dict.keys()))
#Print sorted list of items
print(sorted(dict.items()))
     

