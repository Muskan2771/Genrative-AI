n = 5
for i in range(1, n+1):
    print("  "*(i-1), end="")
    for j in range(i, n+1):
        print(j, end=" ")
    print()
