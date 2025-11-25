#WAP to print all numbers in a range divisible by a given number.

range_start=int(input("Enter the range you want to start: "))
range_stop=int(input("Enter the range you want to stop: "))
divisor=int(input("Enter the divisor: "))

for i in range(range_start,range_stop+1):
     if i%divisor==0:
          print(i)

