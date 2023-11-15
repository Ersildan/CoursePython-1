from math import*

def compute_binom(n, k):
    a = factorial(n)
    b = (factorial(k)) * (factorial(n - k))
    return int(a/b)


n = int(input())
k = int(input())
print(compute_binom(n, k))
