#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be:
# 0,35,70
# 

# In[1]:


#ans:- 
def getno(n): 
    i = 0 
    while i < n:
        j = i
        i += 1 
        if j % 7 == 0 and j % 5 == 0:
            yield j
n = int(input('enter n : '))
num =[]
for i in getno(n): 
    num.append(str(i))
    
print(','.join(num))


# Question 2:
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10
# 

# In[2]:


#ans:-
def getno(n): 
    i = 0 
    while i < n:
        j = i
        i += 1 
        if j % 2 == 0:
            yield j
n = int(input('enter n : '))
num =[]
for i in getno(n): 
    num.append(str(i))
    
print(','.join(num))


# Question 3:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# 
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# 

# In[3]:


#ans:-
def fib(n):    
    if n == 0: 
            return 0    
    elif n == 1: 
            return 1    
    else: 
            return fib(n-1)+fib(n-2)
n=int(input('Enter a number :')) 
values = [str(fib(x)) for x in range(0, n+1)] 
print(",".join(values))


# Question 4:
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# 

# In[4]:


#ans:=
email = input("Enter the email address : ").split('@')
company = str(email[1]).split('.')
print("User name : ",email[0])
print("Company name : ",company[0])


# Question 5:
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# 

# In[6]:


#ans:-
class Shape(object):
  def __init__(self):
    pass

  def area(self):
     return 0

class Square(Shape):
  def __init__(self,l):

    
    self.length = l

  def area(self):
    return self.length*self.length
    


obsquare = Square(7)


obsquare.area()

