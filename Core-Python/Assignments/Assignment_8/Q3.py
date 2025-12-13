#a
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print("Sum:", s)

sum_n(5)

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
def power_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i ** i
    print("Power sum:", s)

power_sum(3)

