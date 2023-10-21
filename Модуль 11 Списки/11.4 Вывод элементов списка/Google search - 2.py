lst = []
count = 0

a = [input() for _ in range(int(input()))]
b = [input() for _ in range(int(input()))]

for i in a:
    for j in b:
        if j.lower() in i.lower():
            count += 1
            if count == len(b):
                lst.append(i)
    count = 0
print(*lst, sep='\n')  
