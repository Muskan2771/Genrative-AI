words = ["apple", "banana", "apple", "orange", "banana"]

unique_words = set(words)

for word in unique_words:
    print(word, ":", words.count(word))
