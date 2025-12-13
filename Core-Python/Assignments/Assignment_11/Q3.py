data = [[1, 4], [3, 1], [5, 2], [2, 3]]

n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        if data[j][1] > data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Sorted by second element:", data)
