names = ["Muskan","Saniya","Rehan","Muskan","Asha","Saniya"]

freq = {}

for name in names:
    if name in freq:
        freq[name] += 1
    else:
        freq[name] = 1

print(freq)
