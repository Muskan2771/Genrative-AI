from math import comb

n = 4
for i in range(n):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print(comb(i, j), end=" ")
    print()
