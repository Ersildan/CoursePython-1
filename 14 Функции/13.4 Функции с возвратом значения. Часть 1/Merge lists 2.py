# put your python code here
def quick_merge():
    a.sort()
    return a
# считываем данные
a = []
n = int(input())
for i in range(n):
    lst = [int(s) for s in input().split()]
    a.extend(lst)
# вызываем функцию
print(*quick_merge())
