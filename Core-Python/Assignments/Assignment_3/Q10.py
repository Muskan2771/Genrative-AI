#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

choice=input("Choice if you are Male or Female: ")

if choice=="Male":
    age_m=int(input("Enter age: "))
    if age_m>=21:
        print("You are eligible to marry")
    else: 
        print("You are not eligible to marry")
elif choice=="Female":
    age_f=int(input("Enter age: "))
    if age_f>=18:
        print("You are eligible to marry")
    else: 
        print("You are not eligible to marry")    
else:
    print("Invalid Input")        
