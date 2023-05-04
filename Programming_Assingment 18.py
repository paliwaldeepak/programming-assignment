#!/usr/bin/env python
# coding: utf-8

# Question 1
# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
# Examples
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# 
# filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
# 
# filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
# 
# 

# In[1]:


#ans:-
l = [1,2,'a','b']

def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list

print(filter_list(l))


# Question 2
# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
# Examples
# reverse("Hello World") ➞ "DLROw OLLEh"
# 
# reverse("ReVeRsE") ➞ "eSrEvEr"
# 
# reverse("Radar") ➞ "RADAr"
# 

# #ans:
# def reverse(str):
#     str = str[::-1]
#     return str.swapcase()
#     
# print(reverse('Hello World'))

# In[ ]:


Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]

print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
first  ➞ 1

middle ➞ [2, 3, 4, 5]

last ➞ 6
Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.


# In[3]:


#ans:
lst = [1, 2, 3, 4, 5, 6]
first ,*middle,last = lst
middle


# Question 4
# Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120
# 
# factorial(3) ➞ 6
# 
# factorial(1) ➞ 1
# 
# factorial(0) ➞ 1
# 

# In[5]:


#ans:
def factorial(n):     
    if n == 0:
        return 1    
    return n * factorial(n-1)

num = int(input('enter a number :'))
print("Factorial of", num, "is", factorial(num))


# Question 5
# Write a function that moves all elements of one type to the end of the list.
# Examples
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# 
# move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
# 
# move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
# 
# 

# In[7]:


#ans:
def move_to_end(array, toMove):
     
    i = 0
     
    j = len(array) - 1
    
    while (i < j):
  
        while (i < j and array[j] == toMove):
  
           
            j-=1
  
        if (array[i] == toMove):
  
            # swap the two elements
            # in the array
            array[i], array[j] = array[j] , array[i]
  
       
        i += 1
  
    # return the result
    return array


# In[14]:


arr = [7, 5, 9, 3, 4]
a = 5
ans = move_to_end(arr, a)
for i in range(len(arr)):
    print(ans[i] ,end= " ")

