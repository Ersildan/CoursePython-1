s = input().split()
b = 'ки'
for i in range(len(s)):
    a = s[i][1:]
    s[i] = s[i][:-1]
    a += s[i][0]+b
    print(a, end=' ')
