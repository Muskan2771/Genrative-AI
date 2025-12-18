def rev_digits(n,rev=0):
    if n == 0:
        return rev
    rev=rev*10+n%10
    return rev_digits(n//10,rev) 
n=int(input("Enter the number: "))
result=rev_digits(n)
print(result)
