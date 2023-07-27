# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:51:35 2021

@author: Divyansh Singhal
"""

n=input("Enter the number:")
l=len(n)
le=()
ce=0
ee=0
ch=None
if "." in n:
    while ch!="y" or ch!="n":
        ch=input("Do you want to exhange the digits between LHS and RHS of the decimal? Press y or n:")
        if ch=="y":
            ci=0
            ca=0
            s=0
            ei=0
            t=()
            p=n.find(".",1,l)
            for a in range(0,p):
                t+=(int(n[a]),)
            for a in range(p+1,l):
                t+=(int(n[a]),)
            for a in range(p+1,l):
                m=min(t)
                li=list(t)
                w=li.remove(m)
                t=tuple(li)
                ei+=m*(10**ci)
                ci+=1
            for a in range(0,p):
                m=min(t)
                le=list(t)
                w=le.remove(m)
                t=tuple(le)
                s+=m*(10**ca)
                ca+=1
            print("The largest number possibe is:",str(s)+"."+str(ei))
        elif ch=="n":
            l1=( )
            c=0
            e=0
            p=n.find(".",1,l)
            for a in range(p):
                l1=l1+(int(n[a]),)
            for b in range(p):
                m=min(l1)
                q=list(l1)
                w=q.remove(m)
                l1=tuple(q)
                e=e+m*(10**c)
                c+=1
                l2=( )
                c1=0
                e1=0
                for f in range(p+1,l):
                    l2+=(int(n[f]),)
                for f1 in range(p+1,l):
                    m=min(l2)
                    q1=list(l2)
                    w=q1.remove(m)
                    l2=tuple(q1)
                    e1=e1+m*(10**c1)
                    c1+=1
                print("The desired number is:",str(e)+"."+str(e1))
        else:
            print("Please enter y or n:")
            ch=input("Do you want to exhange the digits between LHS and RHS of the decimal? Press y or n:")
            continue
else:
    for h in n:
        le=le+(int(h),)
    for g in range(l):
        me=min(le)
        qe=list(le)
        we=qe.remove(me)
        le=tuple(qe)
        ee=ee+me*(10**ce)
        ce+=1
    print("The desired number is:",ee)