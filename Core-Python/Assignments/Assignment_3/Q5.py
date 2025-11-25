#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

print("To check Triangle is quilateral, isosceles or scalene.")
print("Give sides and angles of Triangle:")

side1=int(input("Enter the side 1st"))
side2=int(input("Enter the side 2nd"))
side3=int(input("Enter the side 3rd"))

angle1=int(input("Enter the angle 1st"))
angle2=int(input("Enter the angle 2nd"))
angle3=int(input("Enter the angle 3rd"))

if (angle1 + angle2 + angle3 == 180) and (angle1 > 0 and angle2 > 0 and angle3 > 0):
    
    if side1 == side2 == side3 and angle1 == angle2 == angle3:
        print("This is an Equilateral Triangle.")
    
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("This is an Isosceles Triangle.")

    else:
        print("This is a Scalene Triangle.")
else:
    print("This is NOT a valid triangle.")
