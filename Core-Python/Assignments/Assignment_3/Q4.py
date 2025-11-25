#Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1=int(input("Enter side 1st: "))
side2=int(input("Enter side 2nd: "))
side3=int(input("Enter side 3rd: "))

if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")    
