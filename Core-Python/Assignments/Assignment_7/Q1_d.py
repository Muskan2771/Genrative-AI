n = 5
for i in range(1, n+1):
    print(" " * (n-i) * 2, end="")
    
    # Increasing
    num = i
    for j in range(i):
        print(num, end=" ")
        num += 1

    # Decreasing
    num -= 2
    for j in range(i-1):
        print(num, end=" ")
        num -= 1

    print()
