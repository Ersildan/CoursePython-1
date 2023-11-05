a = [int(i) for i in input().split()]
a.sort()
print(*a)
a.sort(reverse=True)
print(*a)
