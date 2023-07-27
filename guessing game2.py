# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:54:57 2021

@author: Divyansh Singhal
"""
import random
n=random.randint(1,10)
for a in range(5):
    guess=int(input("Enter the number:"))
    if guess>n:
        print("High")
    elif guess<n:
        print("Low")
    else:
        print("Congratulations!! You won")
if guess!=n:
    print("Sorry!! You Lost")