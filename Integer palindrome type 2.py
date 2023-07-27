#Program to create palindrome of an integer using while loop
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