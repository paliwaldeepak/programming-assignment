#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to find words which are greater than given length k?

# In[2]:


#ans:
def Biggerthank(k,str):
    txt = str.split()
    Wordlist = []
    for i in txt:
        if len(i) > k:
            Wordlist.append(i)
    return Wordlist

str = input("Enter the string : ")
k = int(input("Enter the lenth K : "))

Wordlist = Biggerthank(k,str)

print("\nThe original string ' {} '".format(str))

print("Words greater than k{}".format(k))
print(Wordlist)


# 2.	Write a Python program for removing i-th character from a string?

# In[3]:


#ans:-
def remove(str, i): 
  
    for j in range(len(str)):
        if j == i:
            str = str.replace(str[i], "", 1)
    return str      

str = input("Enter the string : ")
i = int(input("Enter the index : "))      

# Print the new string

print("The new string : ", remove(str, i))


# 3.	Write a Python program to split and join a string?

# In[4]:


#ans:-
str = "I love coding"
str = str.split(" ") 
print("Spliting a string : ",str)


str2 = "-".join(str)
print("Joining a string : ",str2)
     


# 4.	Write a Python to check if a given string is binary string or not?

# In[5]:


#ans:=

def ifbinary(str):
    binary = '01'
    for i in range(len(str)):
        if str[i] not in binary:
            print('Not Binary')
            break
    else:
        print('Binary')
        
str = input("Enter the string : ")
ifbinary(str)


# 5.	Write a Python program to find uncommon words from two Strings?

# In[6]:


def unCommon(a,b):
    list_one = a.split()
    list_two = b.split()
    notcom =''
    
    for i in list_one:
        if i not in list_two:
            notcom = notcom +" "+ i
    for j in list_two:
        if j not in list_one:
            notcom = notcom +" "+ j
    return notcom

a = input("Enter the string a : ").lower()
b = input("Enter the string b : ").lower()

print("The list of un Common words : ", unCommon(a,b))


# 6.	Write a Python to find all duplicate characters in string?

# In[8]:


#ans:=
str = input("Enter the string a : ").lower()
duplicate = []

for i in str:
    if str.count(i) > 1 :
        if i not in duplicate:
            duplicate.append(i)
        
duplicate


# 7.	Write a Python Program to check if a string contains any special character?

# In[10]:


#ans:-
import string

str_char = string.punctuation
speci_str = []

str = input("Enter the string a : ").lower()
for i in str:
    if i in str_char:
        speci_str.append(i)
if len(speci_str) > 0:
    print("String {} has special charecter/s : {}".format(str,speci_str))

