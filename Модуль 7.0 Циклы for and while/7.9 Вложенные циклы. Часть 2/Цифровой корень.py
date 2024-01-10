n = int(input())
while n > 9:
    total = 0
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10
    n = total
print(n)
