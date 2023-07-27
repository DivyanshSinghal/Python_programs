# -*- coding: utf-8 -*-

n=input("Enter the number:")
l=len(n)
t=( )
ei=0
s=0
ci=0
ca=0
if "." in n:
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
        w=li.remove(m)
        t=tuple(li)
        s+=m*(10**ca)
        ca+=1
print("The largest number possibe is:",str(s)+"."+str(ei))