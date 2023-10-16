n = int(input())
max1 = 0
max2 = 1
for i in range(1, n + 1):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
print(max1)
print(max2)
