total = 0
num = int(input())
while num >= 25:
    total += 1
    num = num -25
while 10 <= num <= 25:
    total += 1
    num = num - 10
while 5 <= num <=10:
    total += 1
    num = num - 5
while 1<= num <=5:
    total += 1
    num = num -1
print(total)   
