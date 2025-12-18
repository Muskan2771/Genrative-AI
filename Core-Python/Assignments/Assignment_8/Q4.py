def sum_series(n):
    sum_s=0
    for i in range(1,n+1):
            if i%2!=0:
              sum_s+=i
    return sum_s

n=int(input("Enter n value: "))
result=sum_series(n)   
print("Sum of series is: ",result) 
