#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to Add Two Matrices?

# In[3]:


#ans:- 
import numpy as np

mat1 = np.array([[1,4,6],
        [7,5,88],
        [8,5,77]])
mat2 = np.array([[12,43,74],
        [5,8,3],
        [8,9,9]])

Matsum = np.add(mat1,mat2)
print("The Sum of two matrix \n\n{}  and \n\n{}  is \n\n{} ".format(mat1,mat2,Matsum))


# 2.	Write a Python Program to Multiply Two Matrices?

# In[4]:


#ans:
import numpy as np

mat1 = np.array([[13,42,64],
        [3,7,4],
        [9,1,2]])
mat2 = np.array([[2,4,7],
        [55,67,8],
        [8,9,1]])

mulMat = np.dot(mat1,mat2)
print("The product of two matrix \n\n{}  and \n\n{}  is \n\n{} ".format(mat1,mat2,mulMat))


# 3.	Write a Python Program to Transpose a Matrix?

# In[2]:


#ans:

def Matrix(n,v=0):
    M=[]             
    for i in range(n):
        
        row =[]
        for j in range(n):
            row.append(v)
        M.append(row)
    return(M)

def crMatrix(n):
    
    M=[]             
    print("Enter the element :")
    for i in range(n):
        #stor row
        row =[]
        for j in range(n):
            row.append(int(input()))
        M.append(row)
    return(M)

def prMatrix(M,n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=" ")
        print() 

def tpMatrix(M,n,result):
    for i in range(n):
        for j in range(n):
            result[i][j]= M[j][i]
    return result

n=int(input("Enter N for N x N matrix: "))       
M1 = crMatrix(n)

print("Display Array M1 In Matrix Form")
prMatrix(M1,n)

result = Matrix(n)
result = tpMatrix(M1,n,result)
print("Transposed Matrix")
for r in result:
    print(r)    


# 4.	Write a Python Program to Sort Words in Alphabetic Order?

# In[4]:


#ans:
Arr = input("Enter string ")

words = Arr.split()
words.sort()
for word in words:
    print(word)


# 5.	Write a Python Program to Remove Punctuation From a String?

# In[6]:


#ans:- 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

Arr = input("Enter a string with punctuations ")


rem_punc = ""
for i in Arr:
    if i not in punctuations:
        rem_punc = rem_punc + i

# display 
print(rem_punc)

