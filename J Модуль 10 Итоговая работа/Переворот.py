s = input()
start = s.find('h')
end = s.rfind('h')
centr = s[start : end + 1]
b = centr[::-1]
print(s[0 : start], b, s[end + 1 : len(s)], sep='')
