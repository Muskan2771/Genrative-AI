data = [12,12,32]
data2 = [32,45,12]

union = []

for x in data:
    if x not in union:
        union.append(x)
for x in data2:
    if x not in union:
        union.append(x)
print(union)
