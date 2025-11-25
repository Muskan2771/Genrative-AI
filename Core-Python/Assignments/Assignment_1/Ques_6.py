#Write a Program to input two angles from user and find third angle of the triangle.

ang1=int(input("Enter the first angle of Triangle: "))
ang2=int(input("Enter the second angle of Triangle: "))

ang3=180-(ang1+ang2)

print("The Third angle of Triangle: ",ang3,"deg")