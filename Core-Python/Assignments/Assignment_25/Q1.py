import re

def censor_text(text, forbidden_words):
    pattern = r'\b(' + '|'.join(forbidden_words) + r')\b'
    return re.sub(pattern, lambda m: '*' * len(m.group()), text, flags=re.IGNORECASE)

# Example
text = "This is a bad and ugly example"
forbidden = ["bad", "ugly"]
print(censor_text(text, forbidden))
