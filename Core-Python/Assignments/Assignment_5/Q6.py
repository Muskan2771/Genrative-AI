for num in range(2, 101):
    isprime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isprime = False
            break
    if isprime:
        print(num, end=" ")
