#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to check if the given number is a Disarium Number?

# In[2]:


#ans:-
def Disarium(num):
    sum = 0
    while(num>0):
        l= len(str(num))
        no = num%10
        sum= sum + no**l   
        l-=1
        num = num//10
    return sum

num = int(input("Enter the number :"))


sum = Disarium(num)
if sum == num:
    print(num,"Number is Disarium")
else:
    print(num,"Number is not Disarium")
#A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.  


# 2.	Write a Python program to print all disarium numbers between 1 to 100?

# In[3]:


#ans:- 
def Disarium(num):
    sum = 0
    while(num>0):
        l= len(str(num))
        no = num%10
        sum= sum + no**l   
        l-=1
        num = num//10
    return sum

print("Disarium no in range 1 to 100")

disno = []

for i in range(1,101):
    sum = 0
    sum = Disarium(i)
    if sum == i:
        disno.append(i)        
print(disno)
     


# 3.	Write a Python program to check if the given number is Happy Number?

# In[4]:


#ans:- 
def Happy(num):
    sum = 0
    while(num>0):
        dig = num%10
        sum= sum + dig**2        
        num = num//10
    return sum

num = int(input("Enter the number :"))
result = num


while (result != 1 and result != 4):
    result = Happy(result)

if result == 1:
    print(num,"Is a Happy Number")
else:
    print(num," Is a Unhappy Number")
   #A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
   # If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number. 


# 4.	Write a Python program to print all happy numbers between 1 and 100?

# In[5]:


#ans:-
def Happy(num):
    sum = 0
    while(num>0):
        dig = num%10
        sum= sum + dig**2        
        num = num//10
    return sum

print("Happy numbers in range 1 to 100")
result=num=i=0
happyNo = []
for i in range(1,101):
    result = i
    while (result != 1 and result != 4):
        result = Happy(result)    
    if result == 1:
        happyNo.append(i)
print(happyNo)
     


# 5.	Write a Python program to determine whether the given number is a Harshad Number?

# In[6]:


#ans:-
def digsum(num):
    sum = 0
    while(num>0):
        dig = num%10
        sum= sum + dig      
        num = num//10
    return sum

num = int(input("Enter no. :"))
sum = digsum(num)

if num % sum == 0:
    print(num,"Is a Harshad number")
else:
    print(num,"Is not a Harshad number")

#if a number is divisible by the sum of its digits, then it will be known as a Harshad Number


# 6.	Write a Python program to print all pronic numbers between 1 and 100?

# In[7]:


#ans:- 
def PronicNo(num):
    Pronic = False
    for i in range(1,num+1):
        if i*(i+1) == num:
            Pronic = True
            break
    return Pronic

print("Pronic numbers in range 1 to 100")
pronicno = []
for i in range(1,101):
    if PronicNo(i):
        pronicno.append(i)
print(pronicno)

