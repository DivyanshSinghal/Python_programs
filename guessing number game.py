# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:47:58 2021

@author: Divyansh Singhal
"""
import random
n=random.randint(1,10)
guess=None
while guess!=n:
    guess=int(input("Enter the number:"))
    if guess>=n:
        print("High")
    elif guess<=n:
        print("Low")
    else:
        print("Congratulations!! You win")
        break
