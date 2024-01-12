n = [8, 9, 10, 11]
a = [4, 5, 6]
n[1] = 17
n.extend(a)
del n[0]
n = n * 2
n.insert(3, 25)
print(n)
