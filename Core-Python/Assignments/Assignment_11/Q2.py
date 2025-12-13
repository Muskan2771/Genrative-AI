list1 = [12,7,9,20,33,45,10,18]
list2 = [5,7,10,12,25,33,40]
merged = []

for x in list1:
    merged.append(x)
for x in list2:
    merged.append(x)

n = len(merged)
for i in range(n):
    for j in range(0, n-i-1):
        if merged[j] > merged[j+1]:
            merged[j], merged[j+1] = merged[j+1], merged[j]

print("Merged & Sorted list:", merged)
