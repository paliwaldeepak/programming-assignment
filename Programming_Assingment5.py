#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to Find LCM?

# In[1]:


#ans:- 
x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))

if x > y:
    big = x
else:
    big = y
    
while(True):
    if big % x == 0 and big % y == 0 :
        lcm = big
        break
    big+=1
    
print("The LCM of {} and {} is {}".format(x,y,lcm))


# 2.	Write a Python Program to Find HCF?

# In[4]:


x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))

if x < y:
    small = x
else:
    small = y
hcf = 0   
for i in range(1,small+1):
    if x % i == 0 and y % i == 0 :
        hcf = i
    
print("The hcf of {} and {} is {}".format(x,y,hcf))


# 3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[5]:


#ans:- 
x=int(input("Enter number :"))

print(x, "in binary : ", bin(x))
print(x, "in Octal : ", oct(x))
print(x, "in Hexadecimal : ",hex(x))


# 4.	Write a Python Program To Find ASCII value of a character?

# In[6]:


#ans:- 
str = input("Enter a Charecter : ")
print("Ascii value of {} is {}".format(str,ord(str)))


# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[7]:


#ans:- 
x = float(input("Enter num1 :"))
y = float(input("Enter num2 :"))

op = input("Enter + to add : \nEnter - to Sub :\nEnter * to multi :\nEnter / to div : ") 

add = x + y
sub = x - y
mul = x * y


if op == "+":
    print("{} + {} = {}".format(x,y,add))
elif op == "-":
    print("{} - {} = {}".format(x,y,sub))
elif op == "*":
    print("{} * {} = {}".format(x,y,mul))
elif op == "/":
    if num1 == 0 or num2 == 0:
        print("Division with zero is not possible")
    else:
        div = x / y
        print("{} / {} = {}".format(x,y,div))
else:
    print("Invalid input")

