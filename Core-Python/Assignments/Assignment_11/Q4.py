data = [12,45,23,67,89,34,90]

n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Second largest element:", data[-2])
