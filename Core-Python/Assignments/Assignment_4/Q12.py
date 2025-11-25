#WAP to print Armstrong number within a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers in this range are:")

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num)