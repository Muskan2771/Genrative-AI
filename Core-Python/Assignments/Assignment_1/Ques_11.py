# Find the area and circumference of a circle.

import math

radius = float(input("Enter the radius of circle: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)
