data=[11,22,33,45,67,89,21,34,90]
unique = []
for x in data:
    if x not in unique:
        unique.append(x)

print("List without duplicates:", unique)
