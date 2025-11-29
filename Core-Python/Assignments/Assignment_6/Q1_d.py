n = 5
for i in range(1, n+1):
    ch = ord('A')
    for j in range(1, i+1):
        print(chr(ch), end=" ")
        ch += 1
    print()
