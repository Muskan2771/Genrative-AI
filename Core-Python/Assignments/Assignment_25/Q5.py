import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Example
print(validate_email("test@example.com"))   # True
print(validate_email("test@.com"))           # False
