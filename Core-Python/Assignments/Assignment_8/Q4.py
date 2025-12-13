def sum_odd(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            s += i
    print("Sum of odd numbers:", s)

sum_odd(10)
