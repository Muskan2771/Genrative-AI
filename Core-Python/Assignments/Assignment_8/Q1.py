def rect(l, b):
    area = l * b
    return area

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))

result = rect(l, b)
print("Area of rectangle is:", result)
