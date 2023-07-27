# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:11:33 2021

@author: Divyansh Singhal
"""
for a in range(4,0,-1):
    print((4-a)*" ",end="")
    for b in range(0,a):
        print("*",end=" ")
    print()
