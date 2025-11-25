#Find the sum of three-digit number.
num=int(input("Enter the 3 digit number: "))
a=num//100
b=(num%100)//10
c=(num%10)

print("Sum of 3 digit number: ",a+b+c)