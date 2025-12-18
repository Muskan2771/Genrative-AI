def is_prime(num, i=2):
    if num <= 1:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i + 1)

num = int(input("Enter the number: "))

if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is Not a Prime number")
