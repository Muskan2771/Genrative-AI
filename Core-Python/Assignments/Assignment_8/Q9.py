def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome(121)
