def armstrong(num):
    temp = num
    s = 0
    while num > 0:
        d = num % 10
        s += d * d * d
        num //= 10
    if s == temp:
        print("Armstrong Number")
    else:
        print("Not Armstrong")

armstrong(153)
