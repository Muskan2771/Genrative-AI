import re

def extract_dates(text):
    pattern = r'\b(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|' \
              r'(January|February|March|April|May|June|July|August|' \
              r'September|October|November|December)\s\d{1,2},\s\d{4})\b'
    return re.findall(pattern, text)

# Example
text = "Dates are 01/12/2023, 15-01-2024 and January 5, 2022."
dates = extract_dates(text)
print([d[0] if isinstance(d, tuple) else d for d in dates])
