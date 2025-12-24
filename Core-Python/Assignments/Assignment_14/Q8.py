words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = ''.join(sorted(word))
    groups.setdefault(key, []).append(word)

print(groups.values())
