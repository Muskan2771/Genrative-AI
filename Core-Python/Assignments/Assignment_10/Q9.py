data=[11,22,33,45,67,89,21,34,90]
even = []
odd = []

for x in data:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even list:", even)
print("Odd list:", odd)
