a,b,c = int(input()), int(input()), input()

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/' and b != 0:
    print(a/b)
elif b == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')
