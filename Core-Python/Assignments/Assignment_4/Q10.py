#WAP to check if given number is Perfect Number.
 
num=int(input("Enter the number: "))
sum=0

for i in range(1,num):
    if num%i == 0:
        sum += i

if sum == num:
    print(num, "is Perfect Number")
else:
    print(num, "is Not Perfect Number")    
     