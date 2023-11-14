def get_middle_point(x1, y1, x2, y2):
    x = round(((x1 + x2)/2), 1)
    y = round(((y1 + y2)/2), 1)
    return x, y



x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

print(*get_middle_point(x1, y1, x2, y2))
