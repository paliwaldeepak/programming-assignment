#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to convert kilometers to miles?

# In[2]:


#ans:-
km = int(input("kilometer = "))
miles = km*0.62
print("miles = " , miles)


# 2.	Write a Python program to convert Celsius to Fahrenheit?

# In[5]:


#ans:- 
celsius = int(input("celsius value = "))
fahrenhiet = (celsius * 9/5) + 32
print("fahrenhiet = ", fahrenhiet)


# 3.	Write a Python program to display calendar?

# In[7]:


import calendar
yy = int(input("Enter year = "))
mm = int(input("Enter month in number = "))
print(calendar.month(yy,mm))


# 4.	Write a Python program to solve quadratic equation?

# In[8]:


# Formula:
# x=-b+-sqrt(b**2-4ac)/2*a
import cmath
a=int(input("Enter a = "))
b=int(input("Enter b = "))
c=int(input("Enter c = "))
discriminant = (b**2)-(4*a*c)
sol_one = (-b+cmath.sqrt(discriminant))/(2*a)
sol_two = (-b-cmath.sqrt(discriminant))/(2*a)
print(sol_one ,",", sol_two)


# 5.	Write a Python program to swap two variables without temp variable?

# In[10]:


#ans:=
first_variable = int(input("First Variable ="))
second_variable = int(input("Second Variable ="))
print("First Variable Before swap  : {} \n Second variable Before Swap  : {}".format(first_variable,second_variable))
first_variable , second_variable = second_variable , first_variable

print("After Swap : \n First Variabe : {} \n  Second Variable : {}".format(first_variable , second_variable))


# In[ ]:




