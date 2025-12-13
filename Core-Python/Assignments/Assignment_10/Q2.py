# Write a program to find maximum and minimum element in a list (without using built-in functions).

data=[11,23,45,65,76,87,98,90,12,13,43,32]

max_val=data[0]
min_val=data[0]
for d in data:
     if max_val<d:
        max_val=d
     if min_val>d:
        min_val=d   
print(max_val)  
print(min_val)  