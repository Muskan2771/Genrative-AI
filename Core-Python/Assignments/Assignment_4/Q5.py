#WAP to print Fibonacci series upto n.

n = int(input("Enter number n you want: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

