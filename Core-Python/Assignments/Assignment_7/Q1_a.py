n = 5
mid = n

# Upper half
for i in range(1, n+1):
    for j in range(1, 2*n):
        if j == mid - i + 1 or j == mid + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n-1, 0, -1):
    for j in range(1, 2*n):
        if j == mid - i + 1 or j == mid + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
