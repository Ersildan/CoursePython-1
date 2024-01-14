a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
for i in range(len(a1)):
    b = a1[i] + a2[i]
    print(b, end=' ', sep='')
