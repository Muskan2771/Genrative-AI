def reverse_num(num, rev=0):
    if num == 0:
        return rev
    return reverse_num(num//10, rev*10 + num%10)

print(reverse_num(1234))
