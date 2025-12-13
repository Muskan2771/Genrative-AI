data = [12, 12, 32]
data2 = [32, 45, 12]

inter = []

for x in data:
    if x in data2 and x not in inter:
        inter.append(x)

print(inter)
