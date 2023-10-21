a = b = c = []

for i in range(int(input())):
    s = int(input())
    if s < 0:
        a.append(s)
    elif s == 0:
        b.append(s)
    elif s > 0:
        c.append(s)
      
print(*a, *b, *c, sep='\n')
