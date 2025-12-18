def sum_of_digit(num):
    if num==0:
        return 0
    return num%10 + sum_of_digit(num//10)

num=int(input("Enter the number: "))
result=sum_of_digit(num)
print("Sum of digit is: ",result)
