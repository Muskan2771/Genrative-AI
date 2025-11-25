#Program to Find the Roots of a Quadratic Equation -
#  ax**2+bx+c = 0

import math
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

x=b**2-4*a*c
if x>0:
    root1=(-b+math.sqrt(x))/(2*a)
    root2=(-b-math.sqrt(x))/(2*a)
    print("Two real and dist roots: ",root1 ,"and",root2)

elif x == 0:
    root = -b / (2*a)
    print("Two Equal Real Roots:", root, "and", root)  

else:  # x < 0
    real = -b / (2*a)
    imag = math.sqrt(-x) / (2*a)
    print("Roots are Complex:")
    print(real, "+" ,imag,"i")
    print(real,"-" ,imag,"i")      