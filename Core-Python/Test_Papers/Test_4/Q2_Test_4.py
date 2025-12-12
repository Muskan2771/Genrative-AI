#Q2 - Function to calculate factorial using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
num=int(input("Enter a number: "))
result=fact(num)
print("Factorial of",num,"is",fact(num))    

              