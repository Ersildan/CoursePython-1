n = int(input())
a = []
b = []
for i in range(1, n + 1):
    s = int(input())
    a.append(s)
for i in range(len(a) - 1):
    b.append(a[i] + a[1 + i])   
print(b)
