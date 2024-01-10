def is_magic(date):
    flag = False
    a, b, c = date[0], date[1], date[2] % 100
    if a * b == c:
        flag = True
    return flag


date = [int(i) for i in input().split('.')]
print(is_magic(date))
