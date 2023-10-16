num = int(input())
course = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        course = course - i
    else:
        course = course + i
print(course)
