n = int(input())
a = []
for i in range(n):
    s = int(input())
    a.append(s ** 2 + 2 * s + 1)
    print(s)
print()
print(*a, sep='\n')
