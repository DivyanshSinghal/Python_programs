#Python program to guess the random number in 5 chances
import random
n=random.randint(1,10)
print("You have 5 turns for entering the correct number!!")
for a in range(5):
    guess=int(input("Enter the number:"))
    if guess>n:
        print("High")
    elif guess<n:
        print("Low")
    else:
        print("Congratulations!! You won")
if guess!=n:
    print("Sorry!! You Lost")