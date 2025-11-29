n = int(input("Enter n: "))
s = 0
term = 1

for i in range(n):
    s += term
    term *= 2

print("Sum =", s)
