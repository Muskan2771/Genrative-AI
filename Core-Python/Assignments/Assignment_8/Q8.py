def reverse_num(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    print("Reverse number:", rev)

reverse_num(1234)
