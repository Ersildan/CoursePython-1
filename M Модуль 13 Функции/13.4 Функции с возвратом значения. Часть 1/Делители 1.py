# объявление функции
def get_factors(n):
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    return a
# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
