def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_sum(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrong_sum(n // 10, digits)

num = int(input("Enter a number: "))
digits = count_digits(num)

if num == armstrong_sum(num, digits):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
