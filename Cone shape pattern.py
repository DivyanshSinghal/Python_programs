#Program to create a cone shape pattern
for a in range(4,0,-1):
    print((4-a)*" ",end="")
    for b in range(0,a):
        print("*",end=" ")
    print()
