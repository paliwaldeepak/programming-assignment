#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[4]:


#ans:- 
number = int(input("enter value = "))
if number <0:
    print("number is negative")
elif number > 0:
        print("number is positive")
else :
    print("number is zero")


# 2.	Write a Python Program to Check if a Number is Odd or Even?

# In[13]:


#ans:-
x = int(input("enter value = "))
if x%2 == 0:
    print("no is even")
else:
    print("no is odd")


# 3.	Write a Python Program to Check Leap Year?

# In[15]:


#ans:
x = int(input("enter year = "))
if x%4 == 0:
    print("year is a leap year")
else:
    print("year is not a leap year")


# 4.	Write a Python Program to Check Prime Number?

# In[17]:


#ans:-
x = int(input("Enter a no."))
for i in range(2,x):
    if x % i == 0:
        print("no is not a prime no.")
        break
else:
              print("no is  a prime no.")


# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[19]:


#ans:
x = int(input("Enter a number1: ")) 
y = int(input("Enter a number2: ")) 
for num in range(x,y):  
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                print(num,'is not a prime')                
                break
        else:
            print(num,'is a prime number')


# In[ ]:




