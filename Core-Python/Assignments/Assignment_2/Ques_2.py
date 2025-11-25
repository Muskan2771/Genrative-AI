#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

C_temp=int(input("Enter the temp in Celsius to convert in Fahrenfeit: "))

F_temp=(C_temp * 9/5)+32

print("Temperature in Fahrenheit: ",F_temp, "°F")