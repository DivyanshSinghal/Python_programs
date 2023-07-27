#Program to check whether the entered string is palindrome or not
n=input("Enter the string:") 
if n==n[::-1]:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")