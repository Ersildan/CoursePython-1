n = int(input())
for i in range(1, n + 1):
    conter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            conter += 1
    print(i, conter * '+', sep='')
