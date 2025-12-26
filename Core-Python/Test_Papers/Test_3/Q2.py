n = int(input("Enter the number: "))
total = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    total = total + (i / fact)

print("Sum of the series:", total)
