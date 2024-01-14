n = input()
a = n.replace('#','')
for i in range(int(a)):
    s = input()
    if '#' in s:
        s = s[:s.index('#')]
        s = s.rstrip()
    print(s)
