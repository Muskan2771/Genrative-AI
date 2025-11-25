#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.


range_start=int(input("Enter the range you want to start: "))
range_stop=int(input("Enter the range you want to stop: "))

for i in range(range_start,range_stop+1):
    if i%7==0 and i%5==0:
        print(i)
