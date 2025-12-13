data=[11,22,33,45,67,89,21,34,90]
num = int(input("Enter number: "))

count = 0
for x in data:
    if x == num:
        count += 1

if count > 0:
    print(num,"is present",count,"times")
else:
    print(num,"not present")
