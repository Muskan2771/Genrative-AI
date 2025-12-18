def sum_primes(n):
    total = 0
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total += i
    return total

n = int(input("Enter n value: "))
result = sum_primes(n)
print("Sum of all prime numbers from 1 to", n, "is:", result)
