#Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1=int(input("Enter the 1st angle: "))
ang2=int(input("Enter the 2nd angle: "))
ang3=int(input("Enter the 3rd angle: "))

sum=ang1+ang2+ang3

if sum==180 and ang1>0 and ang2>0 and ang3>0:
    print("This angles of Triangle is Valid")
else:
    print("This is angles of Triangle are not valid ")    
