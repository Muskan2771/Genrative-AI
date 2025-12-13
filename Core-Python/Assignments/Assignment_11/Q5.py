data = ["hi", "python", "ok"]

for i in range(len(data)):
    for j in range(0, len(data)-1):
        if len(data[j]) > len(data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]

print(data)
