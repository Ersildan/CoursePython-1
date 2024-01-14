a = [int(i) for i in input().split()]
b = a.copy()
max_b = max(b)
min_b = min(b)
poisk1 = b.index(max_b)
poisk2 = b.index(min_b)

a[poisk1] = min_b
a[poisk2] = max_b
print(*a)
