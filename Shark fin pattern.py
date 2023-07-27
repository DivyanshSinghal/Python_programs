#Program to create a shark fin pattern
for a in range(1):
    for b in range(a+1):
        print("*")
for a in range(1,3):
    print(" ",end="")
    for b in range(a+1):
        print("*",end="")
    print()
for a in range(4):
    print("*",end="")
print()
        