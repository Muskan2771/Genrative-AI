def rev_func(num):
      rev=0
      temp=num
      while temp>0:
            digit=temp%10
            rev=rev*10+digit 
            temp//=10
      return rev  

num=int(input("Enter the num: "))
result=rev_func(num)
print(f"The rev is :{result}")
