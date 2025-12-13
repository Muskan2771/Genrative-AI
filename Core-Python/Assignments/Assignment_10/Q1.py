#1. Write a program to find sum of all elements of list without buit in function.
data=[11,22,33,45,67,89,21,34,90]

x=0
for d in data:
    x+=d
print("Sun of all elements: ",x)    


total=0
for i in range(0,len(data)):
    x=data[i]
    total+=x 
print("Sum of all elements: ",total)    
