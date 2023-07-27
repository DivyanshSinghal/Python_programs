# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:09:39 2021

@author: Divyansh Singhal
"""
n=int(input("Enter the number:"))
l=len(str(n))
t=l-1
s=0
while t>=0:
   d=n%10
   n//=10
   s+=d*(10**t)
   t-=1
print("The palindrome number is:",s)