def sum_digit(num):
    temp=num
    total=0
    while temp>0:
          digit=temp%10
          temp//=10
          total+=digit
    return total   

num=int(input("Enter the number: "))
result=sum_digit(num)   
print("The sum of digit is: ",result)  
