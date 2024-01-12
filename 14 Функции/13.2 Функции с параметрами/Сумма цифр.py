def print_digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10 
    print(total)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
