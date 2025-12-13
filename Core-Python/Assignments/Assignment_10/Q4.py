data=[11,22,33,45,67,89,21,34,90]

rev=[]
for i in range(len(data)-1, -1, -1):
    rev.append(data[i])

print("Reversed list:", rev)
