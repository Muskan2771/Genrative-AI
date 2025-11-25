# Convert distance given in feet and inches into meters and centimeters

feet = int(input("Enter the distance in feet: "))
inch = int(input("Enter the distance in inches: "))

meter = (feet * 0.3048) + (inch * 0.0254)

centimeter = meter * 100

print("Distance in meters:", meter, "m")
print("Distance in centimeters:", centimeter, "cm")