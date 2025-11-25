#Write a program to calculate area of an equilateral triangle.

import math

side=int(input("Enter the side of Equilateral triangle: "))

Area=(math.sqrt(3)/4)*(side**side)

print("Area of Equilateral trianlge: ",Area)