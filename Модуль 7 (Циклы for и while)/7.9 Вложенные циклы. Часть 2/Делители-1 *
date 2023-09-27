a, b = int(input()), int(input())
counter = 0
largest = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        if total >= counter and i >= largest:
            counter = total
            largest = i
print(largest, counter)
