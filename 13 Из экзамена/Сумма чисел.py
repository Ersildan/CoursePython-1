lst = [int(i) for i in input().split()]
b = sum(lst)
print(*lst, sep='+', end='')
print('=', b, end='', sep='')
