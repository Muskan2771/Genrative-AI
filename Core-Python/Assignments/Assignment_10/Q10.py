data=[11,22,33,45,67,89,21,34,90]
num = int(input("Enter element to remove: "))

new_list = []
for x in data:
    if x != num:
        new_list.append(x)

print("Updated list:",new_list)
