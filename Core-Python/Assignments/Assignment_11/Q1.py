list= [12,7,9,20,33,45,10,18]
even = []
odd = []

for x in list:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Even list:", even)
print("Odd list:", odd)


