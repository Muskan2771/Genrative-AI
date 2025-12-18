#a
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = int(input("Enter the value of n: "))
result = sum_n(n)
print("Sum of numbers from 1 to", n, "is:", result)

#b
def fact_sum(n):
    total = 0
    for i in range(1, n+1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        total += fact
    print("Factorial sum:", total)

fact_sum(4)

#c
def sum_power_series(n):
    sum_s = 0
    for i in range(1, n+1):
        sum_s += i**i
    return sum_s

n = int(input("Enter n value: "))
result = sum_power_series(n)
print("Sum of series 1^1 + 2^2 + ... + n^n is:", result)



