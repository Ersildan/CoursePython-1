'''Напишите программу, которая упорядочивает три числа от большего к меньшему'''
a, b, c = int(input()), int(input()), int(input())

a_max = int(min(a, b, c))
a_min = int(max(a, b, c))

sredniy = a + b + c - a_min - a_max

print(a_min)
print(sredniy)
print(a_max)
