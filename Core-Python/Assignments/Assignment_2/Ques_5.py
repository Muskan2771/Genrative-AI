#WAP to calculate selling price of book based on cost price and discount.
#SP = CP-D

CP=float(input("Enter the cost price of Book: "))
D=FloatingPointError(input("Enter the discount on Book in %: "))

DA = CP* (D/100)
SP = CP-DA

print("The selling Price of Book is: ",SP)