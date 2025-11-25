# Program to check if 3-digit number is a palindrome

num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num % 100) // 10
c = num % 10

rev = c* 100 + b * 10 + a

if num == rev:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")