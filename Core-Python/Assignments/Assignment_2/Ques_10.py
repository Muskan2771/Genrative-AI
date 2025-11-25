#Write a program to reverse three-digit number.

num=int(input("Enter the 3 digit number: "))
a=num//100
b=(num%100)//10
c=num%10

rev=(c*100)+(b*10)+a

print("Reverse of 3 digit number is:",rev)