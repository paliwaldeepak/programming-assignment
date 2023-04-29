#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to find sum of elements in list?

# In[1]:


#ans:- 
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("Sum of elements in List",sum(lst))


# 2.	Write a Python program to  Multiply all numbers in the list?

# In[2]:


#ans:- 
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
product = 1
for i in lst:
    product = product*i
print("Product of elements in List is :",product)


# 3.	Write a Python program to find smallest number in a list?

# In[3]:


#ans:- 
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("The Smallest no. in the list is :",min(lst))


# 4.	Write a Python program to find largest number in a list?

# In[1]:


#ans:- 
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("The largest no. in the list is :",max(lst))


# 5.	Write a Python program to find second largest number in a list?

# In[2]:


#ans:- 
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
lst.sort()
print("The sorted list is ",lst)
print("The second largest number in the list is ",lst[-2])


# 6.	Write a Python program to find N largest elements from a list?

# In[4]:


#ans:-
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
lst.sort()
print("The sorted list is ",lst)
nlar = int(input("Enter how many largest number you want from list:"))

if n < nlar :
    print("enterted value is larger then the length of list")
else:
    print(nlar,"largest elements from the list are :",lst[(n-nlar):])


# 7.	Write a Python program to print even numbers in a list?

# In[5]:


#ans:=
lent =  int(input("Enter  the len of the list :"))
lst = []
for i in  range(lent):
  lst.append(int(input()))
print("The List is :" ,lst)
even = [i for i in lst if i%2==0 ]
print("The even numbers in list" , even)


# 8.	Write a Python program to print odd numbers in a List?

# In[6]:


#ans:-
lent =  int(input("Enter  the len of the list :"))
lst = []
for i in  range(lent):
  lst.append(int(input()))
print("The List is :" ,lst)
odd = [i for i in lst if i%2 != 0 ]
print("The even numbers in list" , odd)


# 9.	Write a Python program to Remove empty List from List?

# In[7]:


#ans:-
lst = [55,[],14,75,[],96,80,[],36]
print("The List :",lst)
new_list = [item for item in lst if item != []]
print("The list after removing empty lists :" , new_list)


# 10.	Write a Python program to Cloning or Copying a list?

# In[8]:


#ans:-
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)

lst_copy = lst.copy()
print("Cloning By list copying lst ",lst_copy)


# 11.	Write a Python program to Count occurrences of an element in a list?

# In[9]:


#ans:-
lent = int(input("Enter the lenth of your list : "))
lst = []

for i in range(lent):
    lst.append(int(input()))
print("The List is ",lst)
ele= int(input("Enter the element to find its occurance : "))
print(ele,"has occured {} times in the list ".format(lst.count(ele)))

