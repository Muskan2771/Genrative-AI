# Left
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()

# Right
for i in range(1, 5):
    print("  "*(4-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
