#Program to create a palindrome of an integer in some other way
n=int(input("Enter the number:"))
l=len(str(n))
s=0
c=0
r=l
for a in range(r):
    b=n%10
    s+=b*(10**(l-1))
    n=n//10
    l=l-1
print(s)
    