import re

def word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

# Example
text = "Python is easy and Python is powerful"
print(word_count(text))
