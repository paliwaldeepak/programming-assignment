#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to find sum of array?

# In[1]:


#ans:-
def sum_array(arr):
   
    sum = 0
    for i in arr:
        sum += i
    return sum


# In[2]:


arr = [1, 2, 3, 4, 5]
print(sum_array(arr))  


# 2.	Write a Python Program to find largest element in an array?

# In[3]:


#ans:-
c = 0
arr = [1,2,3,4,77,9]
for i in range(0, len(arr)):
  if c > arr[i]:
    print(c)
  else :
    c = arr[i]

print("Largest element in {} is {}".format(arr ,c) )   


# 3.	Write a Python Program for array rotation?

# In[4]:


#ans:
def rotate_array(arr, n):
    
    n = n % len(arr)  # Ensure rotation amount is within array bounds
    return arr[n:] + arr[:n]

# Example 
arr = [1, 2, 3, 4, 5]
n = 2
rotated_arr = rotate_array(arr, n)
print(rotated_arr)


# 4.	Write a Python Program to Split the array and add the first part to the end?

# In[5]:


#ans:- 
def split_and_add(arr, n):
    return arr[n:] + arr[:n]

# Example
arr = [1, 2, 3, 4, 5]
n = 2
new_arr = split_and_add(arr, n)
print(new_arr)  # Output: [3, 4, 5, 1, 2]


# 5.	Write a Python Program to check if given array is Monotonic?

# In[7]:


#ans:
l = int(input("Enter the lenth of your list : "))
arr = []

for i in range(l):
    arr.append(int(input()))
print("The List is ",arr)

if all((arr[i] <= arr[i+1] for i in range(l-1)) or (arr[i] >= lst[i+1] for i in range(l-1))):
    print("Monotonic")
else:
    print("Not Monotonic")
     

