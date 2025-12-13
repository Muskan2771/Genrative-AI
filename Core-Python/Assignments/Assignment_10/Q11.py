data=[11,22,33,45,67,89,21,34,90]
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for x in data:
    if x % m == 0 and x % n == 0:
        print(x)
