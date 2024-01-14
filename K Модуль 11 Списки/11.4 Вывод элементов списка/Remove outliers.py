n = int(input())
a = []

for i in range(n):
    s = int(input())
    a.append(s)
  
a.remove(max(a))
a.remove(min(a))

print(*a, sep='\n')
