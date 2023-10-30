n = int(input())

total3 = 0
total_last_diget = 0
total_chet = 0
summa_more_5 = 0
proiz_1 = 1
total_0_5 = 0
last_diget = n % 10

while n != 0:
    if n % 10 == 3:
        total3 += 1
    if n % 10 == last_diget:
        total_last_diget += 1
    if n % 2 == 0:
        total_chet += 1
    if n % 10 > 5:
        summa_more_5 += n % 10
    if n % 10 > 7:
        proiz_1 *= n % 10
    if n % 10 == 0 or n % 10 == 5:
        total_0_5 += 1 
    n //= 10

print(total3, total_last_diget, total_chet, summa_more_5, proiz_1, total_0_5, sep='\n')
