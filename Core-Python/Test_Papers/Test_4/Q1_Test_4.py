#Q1- Function to print factors of a number
def fact(n):
    print("Factors of",n,"are: ",end=" ")
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
    print()

num=int(input("Enter a number: "))
fact(num) 

