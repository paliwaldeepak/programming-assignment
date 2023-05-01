#!/usr/bin/env python
# coding: utf-8

# Question 1:
# 
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n
# 

# In[1]:


#ans:-
def gen(n):
  
  for i in range(0,n):
    if i%7==0:
      print(i)
n = int(input('enter n : '))
gen(n)   


# Question 2:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# 
# Suppose the following input is supplied to the program:
# 
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 
# Then, the output should be:
# 
# 2:2
# 
# 3.:1
# 
# 3?:1
# 
# New:1
# 
# Python:5
# 
# Read:1
# 
# and:1
# 
# between:1
# 
# choosing:1
# 
# or:2
# 
# to:1
# 

# In[2]:


#ans:-
Sentence = input('Enter the sentence ').split()
word = sorted(set(Sentence))     # sort alphbetically

for i in word:
    print("{0}:{1}".format(i,Sentence.count(i)))


# Question 3:
# 
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
# 

# In[3]:


#ans:- 
class Person(object):
    def getGender( self ):
        return "None"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

ob_male = Male()
ob_female= Female()
print(ob_male.getGender())
print(ob_female.getGender())


# Question 4:
# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
# 

# In[4]:


#ans:
subject=["I", "You"]
verb=["Play", "Love"]
obj=["Hockey","Football"]


str_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in str_list:
    print(sentence)


# Question 5:
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
# 

# In[5]:


#ans:
import zlib
str = 'hello world!hello world!hello world!hello world!'

a = bytes(str, 'utf-8')
b = zlib.compress(a)
print(b)
print(zlib.decompress(b))


# Question 6:
# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
# 

# In[6]:


#ans:-
from bisect import bisect_left
  
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1 

a = [1, 2, 4, 4, 8]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", res)

