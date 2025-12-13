# Write a program to find the second largest element in the list (without using built-in functions).

data=[11,22,33,45,67,89,21,34,90]

largest = data[0]
second_largest = -1   

for d in data:
    if d > largest:
        second_largest = largest
        largest = d
    elif d > second_largest and d != largest:
        second_largest = d

print("Second largest element:", second_largest)

        








