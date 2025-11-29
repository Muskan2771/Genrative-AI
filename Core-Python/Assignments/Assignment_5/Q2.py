# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input("Enter the number of students: "))
total_per=0

for i in range(1,n+1):
     print("Student", i)
     name=input("Enter name of student: ")
    
     s1=int(input("Enter the marks of subject1: "))
     s2=int(input("Enter the marks of subject2: "))
     s3=int(input("Enter the marks of subject3: "))
     s4=int(input("Enter the marks of subject4: "))
     s5=int(input("Enter the marks of subject5: "))
    
     percetage = ((s1+s2+s3+s4+s5)/500)*100
     total_per+=percetage
     print("Percetage of" ,name,"is: ",percetage)

avg=total_per/n
print("Average of students is: ",avg)    
    
    

