def sum_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    print("Sum of digits:", s)

sum_digits(123)
