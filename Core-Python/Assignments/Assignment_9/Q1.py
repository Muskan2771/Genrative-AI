def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)
        
def sum_fact(n):
    if n == 1:
        return 1
    else:
        return fact(n) + sum_fact(n - 1)

num = int(input("Enter the number: "))
result = sum_fact(num)
print("Sum of factorials:", result)
