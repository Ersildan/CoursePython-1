# объявление функции
def number_of_factors(n):
    a =[i for i in range(1,n+1) if n % i == 0]
    return len(a)
    
# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
