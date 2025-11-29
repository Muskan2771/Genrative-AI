n = int(input("Enter n: "))
count = 0
num = 2

while count < n:
    isprime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isprime = False
            break

    if isprime:
        print(num, end=" ")
        count += 1

    num += 1
