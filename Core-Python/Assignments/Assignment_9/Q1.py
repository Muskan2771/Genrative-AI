def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def fact_sum(n):
    if n == 1:
        return fact(1)
    return fact(n) + fact_sum(n-1)

print(fact_sum(4))
