def prime(num, i=2):
    if num <= 2:
        return True
    if i == num:
        return True
    if num % i == 0:
        return False
    return prime(num, i+1)

print(prime(7))
