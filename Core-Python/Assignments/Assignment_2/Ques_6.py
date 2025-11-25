#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

basic = float(input("Enter the basic salary of the employee: "))

DA = basic * 0.10  
TA = basic * 0.12   
HRA =basic * 0.15  

total_salary = basic + DA + TA + HRA

print("DA:", DA)
print("TA:", TA)
print("HRA:", HRA)
print("Total Salary of Employee:", total_salary)

