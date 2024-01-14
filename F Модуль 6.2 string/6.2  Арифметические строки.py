a,b,c = len(input()), len(input()), len(input())
if (2*b - a - c)*(2*c - a - b)*(2*a - b - c) == 0:
    print('YES')
else:
    print('NO')
