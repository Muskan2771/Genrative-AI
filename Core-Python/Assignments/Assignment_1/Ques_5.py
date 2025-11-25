#Write a program to enter P, T, R and calculate Compound Interest.

Prin=int(input("Enter the Principal: "))
Time=int(input("Enter the Time: "))
Rate=int(input("Enter the Rate: "))

Amount=Prin*(1+Rate/100)**Time
Comp_Int = Amount - Prin

print("The Compund Intreset: ",Comp_Int)


