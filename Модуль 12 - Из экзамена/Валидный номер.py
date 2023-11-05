s = [i for i in input().split('-')]
s2 = "".join(s)
if s2.isdigit():
    s2 = True
else:
    print('NO')
    quit()
if s[0] == '7':
    del s[0]
if len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
    print('YES')
else:
    print('NO')
