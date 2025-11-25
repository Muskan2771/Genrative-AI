# WAP to check if a given number is Strong Number
# Example: 145 = 1! + 4! + 5! = 145

num = int(input("Enter the number: "))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += factorial(digit)
    temp //= 10

if num == sum:
    print(num, "is Strong Number")
else:
    print(num, "is NOT  Strong Number")
