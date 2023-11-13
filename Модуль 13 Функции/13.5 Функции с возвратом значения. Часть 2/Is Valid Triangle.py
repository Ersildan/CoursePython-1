# объявление функции
def is_valid_triangle(a, b, c):
    if (a < b+c) and (b < a+c) and (c < a+b):
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
