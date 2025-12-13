def sum_prime(n):
    total = 0
    for num in range(2, n+1):
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            total += num
    print("Sum of prime numbers:", total)

sum_prime(10)
