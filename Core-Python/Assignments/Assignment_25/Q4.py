import re

def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

# Example
text = "Visit https://www.google.com and http://example.com for info."
print(extract_urls(text))
