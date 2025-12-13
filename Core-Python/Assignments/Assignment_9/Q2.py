def armstrong(num, temp, s=0):
    if num == 0:
        return s == temp
    d = num % 10
    return armstrong(num//10, temp, s + d*d*d)

n = 153
if armstrong(n, n):
    print("Armstrong Number")
else:
    print("Not Armstrong")
