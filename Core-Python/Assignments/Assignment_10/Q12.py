data=[11,22,33,45,67,89,21,34,90]

squares = []
cubes = []

for x in data:
    squares.append(x**2)
    cubes.append(x**3)

print("Numbers:", data)
print("Squares:", squares)
print("Cubes:", cubes)
