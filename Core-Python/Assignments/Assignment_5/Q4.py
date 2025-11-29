num = int(input("Enter number: "))
temp = num
digits = len(str(num))
s = 0

while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10

if s == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
