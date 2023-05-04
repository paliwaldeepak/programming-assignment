#!/usr/bin/env python
# coding: utf-8

# Question1
# Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# 
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
# 
# filter_list(["Nothing", "here"]) ➞ []
# 

# In[2]:


#ans:-
lst = [1, 2, 3, 'a', 'b', 4]
def filter_list(lst):
    int_list = []
    for i in lst:
        if type(i) == int:
            int_list.append(i)
       
    return int_list


# In[3]:


filter_list([1, 2, 3, 'a', 'b', 4])


# Question2
# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
# Examples
# add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
# 
# add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
# 
# add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
# 
# 

# In[4]:


#ans:-
def add_indexes(lst):
    ind = 0
    index = []
    for i in lst:
        index.append(lst.index(i,ind) + i)
        ind+=1
    return index
     


# In[5]:


add_indexes([0, 0, 0, 0, 0])


# In[6]:


add_indexes([5, 4, 3, 2, 1])


# Question3
# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
#  
# Examples
# cone_volume(3, 2) ➞ 12.57
# 
# cone_volume(15, 6) ➞ 565.49
# 
# cone_volume(18, 0) ➞ 0
# 

# In[8]:


#ans:-
import math
pi = math.pi
 
# calculate Volume of Cone
def cone_volume(h, r):
    return round((1 / 3) * pi * r * r * h)
 



height = float(12)
radius = float(8)

print( "Volume Of Cone : ", cone_volume(height, radius) )


# Question4
# This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are: 
# 1, 3, 6, 10, 15
# This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
# Write a function that gives the number of dots with its corresponding triangle number of the sequence.
# Examples
# triangle(1) ➞ 1
# 
# triangle(6) ➞ 21
# 
# triangle(215) ➞ 23220
# 

# In[9]:


#ans:-
def triangle(n):
    return n*(n+1)*0.5

n = int(input('Enter the triangle number :'))
print("The {}th triangle has {} dots ".format(n,int(triangle(n))))
     


# Question5
# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
# Examples
# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
# 
# missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
# 
# missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
# 

# In[10]:


#ans:-
def missing_num(lst):
    total = sum([x for x in range(11)])
    sum_Of_list = sum(lst)
    return total - sum_Of_list

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

