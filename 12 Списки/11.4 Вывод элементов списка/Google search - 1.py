n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
poisk = input()
for j in a:
    if poisk.lower() in j.lower():
        print(*j, sep='')
