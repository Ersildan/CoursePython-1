a = input().split('.')
total = 0
for i in a:
    if int(i) <= 250:
        total += 1
if total == 4:
    print('ДА')
else:
    print('НЕТ')
