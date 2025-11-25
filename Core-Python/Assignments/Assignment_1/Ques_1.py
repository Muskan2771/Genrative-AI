#Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1=int(input("Enter the marks of Subject1: "))
sub2=int(input("Enter the marks of Subject2: "))
sub3=int(input("Enter the marks of Subject3: "))
sub4=int(input("Enter the marks of Subject4: "))
sub5=int(input("Enter the marks of Subject5: "))

sum=sub1+sub2+sub3+sub4+sub5
perc=(sum/500)*100

print("The percentage is:",perc,"%")