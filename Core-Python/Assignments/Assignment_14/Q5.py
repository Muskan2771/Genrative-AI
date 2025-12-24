strings = ["flower", "flow", "flight"]

prefix = ""
for i in zip(*strings):
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break

print(prefix)
