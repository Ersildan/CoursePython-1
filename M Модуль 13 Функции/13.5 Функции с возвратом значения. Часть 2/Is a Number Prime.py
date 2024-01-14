# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

# считываем данные
num = int(input())

# вызываем функцию
print(is_prime(num))
