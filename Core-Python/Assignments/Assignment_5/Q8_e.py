x = float(input("Enter x: "))
n = int(input("Enter n: "))
s = 0
sign = 1
den = 1

for i in range(1, n+1):
    s += sign * (x ** i) / den
    sign *= -1     
    den += 2       

print("Sum =", s)
