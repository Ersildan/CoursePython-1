num = int(input())
counter = 0
for i in range(1,num+1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8 :
        counter = counter + i
print(counter)
