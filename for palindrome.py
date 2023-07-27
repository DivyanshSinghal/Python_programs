# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:34:07 2021

@author: Divyansh Singhal
"""
n=int(input("Enter the number:"))
l=len(str(n))
t=l
c=l-1
s=0
for a in range(t):
    b=n%10
    s+=b*(10**c)
    n//=10
    c-=1
print("The palindrome of the number is:",s)