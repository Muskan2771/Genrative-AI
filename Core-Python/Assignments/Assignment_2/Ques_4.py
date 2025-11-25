# WAP to calculate area of triangle and rectangle

print("1. Area of Triangle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    base = int(input("Enter the Base of Triangle: "))
    height = int(input("Enter the Height of Triangle: "))
    Area_T = (1/2) * (base * height)
    print("The area of Triangle is:", Area_T)

elif choice == 2:
    length = int(input("Enter the length of Rectangle: "))
    width = int(input("Enter the width of Rectangle: "))
    Area_R = length * width
    print("The area of Rectangle is:", Area_R)

else:
    print("Invalid choice! Please enter 1 or 2.")
