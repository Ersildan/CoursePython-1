s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
else:
    s = s.replace('f','a', 1)
    b = s.find('f')
    print(b)
