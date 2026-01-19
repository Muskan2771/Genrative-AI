#Q1
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print("Fibonacci up to 100:")
for num in fibonacci(100):
    print(num, end=' ')
print("\n")

#Q2
def palindrome_numbers():
    n = 0
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n += 1

pal_gen = palindrome_numbers()
print("First 20 palindrome numbers:")
for _ in range(20):
    print(next(pal_gen), end=' ')
print("\n")

#Q3
def my_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

print("Custom range from 5 to 20 step 3:")
for i in my_range(5, 20, 3):
    print(i, end=' ')
print("\n")
