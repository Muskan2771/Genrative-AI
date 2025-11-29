n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    ch = ord('A')
    for j in range(1, 2*i):
        print(chr(ch), end=" ")
        ch += 1
    print()
