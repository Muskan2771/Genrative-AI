data=[11,22,33,45,67,89,21,34,90]
odd_list = []
for x in data:
    if x % 2 != 0:
        odd_list.append(x)

print("List after removing even numbers:", odd_list)
