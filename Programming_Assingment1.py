#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?

# In[1]:


x = "Hello Python"
print(x)


# 2.	Write a Python program to do arithmetical operations addition and division.?

# In[8]:


x = int(input("value 1"))
y = int(input("value 2"))
add = x+y
div = x/y
print(add , div )


# 3.	Write a Python program to find the area of a triangle?

# In[11]:


base = int(input("base of the triangle = "))
hight = int(input("hight of the triangle = "))
area = (base*hight)/2
print(area)


# 4.	Write a Python program to swap two variables?

# In[15]:


a = int(input("first variable a = "))
b = int(input("second variable b = "))
a, b = b, a
print(a,b)


# 5.	Write a Python program to generate a random number?

# In[17]:


import random 
print(random.randint(0,9))

