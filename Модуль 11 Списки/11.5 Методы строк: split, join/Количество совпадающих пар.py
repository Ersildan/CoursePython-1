a = input().split()
total = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            total +=1
print(total)
