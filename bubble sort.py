#Program for doing bubble sort
n=eval(input("Enter the array:")) 
m=list(n) 
l=len(m)
for a in range(l):
    for b in range(l-a-1):
        if m[b]>m[b+1]:
            m[b],m[b+1]=m[b+1],m[b]
print("The sorted array is:",type(n)(m))
    