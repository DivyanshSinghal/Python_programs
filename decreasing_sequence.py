# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:10:57 2021

@author: Divyansh Singhal"""
n=input("Enter the number:")
t=()
t1=()
if "." in n:
    f=n.find(".",1,len(n))
    for a in range(f):
        t+=(int(n[a]),)
    c=0
    s=()
    e=0
    for b in n:
        s+=(int(b),)
    l=len(s)
    for z in range(l):
        x=min(s)
        l1=list(s)
        q=l1.remove(x)
        s=tuple(l1)
        e=e+x*(10**c)
        c+=1
    for i in range(f+1,len(n)):
        t1+=(int(n[i]),)
    c1=0
    s1=()
    e1=0
    for b in n:
        s+=(int(b),)
    l=len(s)
    for z in range(l):
        x=min(s)
        l1=list(s)
        q=l1.remove(x)
        s=tuple(l1)
        e=e+x*(10**c)
        c+=1



print("The required number is:",e)