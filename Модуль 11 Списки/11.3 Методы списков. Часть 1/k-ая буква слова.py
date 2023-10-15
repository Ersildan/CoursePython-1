n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
k = int(input())
for j in range(n):
    e = a[j]
    if len(e) >= k:
        print(e[k-1], end='')
