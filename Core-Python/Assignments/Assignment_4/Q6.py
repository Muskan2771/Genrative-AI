# WAP to check if a given number is prime number or not.

num = int(input("Enter the number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    for i in range(2, (num//2) +1):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
