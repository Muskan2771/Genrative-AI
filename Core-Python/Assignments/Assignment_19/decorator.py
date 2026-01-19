def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Example: Fibonacci using memoization
@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci with memoization (first 20):")
for i in range(20):
    print(fib(i), end=' ')
