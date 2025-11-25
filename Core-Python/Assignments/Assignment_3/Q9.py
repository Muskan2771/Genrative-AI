# Program to input 5 subject marks and display grade

sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
sub4 = int(input("Enter sub4 marks: "))
sub5 = int(input("Enter sub5 marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("Percentage:", round(percentage, 2))

if percentage >= 80:
    print("First Class : A+")
elif percentage >= 60:
    print("Second Class : B+")
elif percentage >= 35:
    print("Third Class : C+")
else:
    print("Failed")
