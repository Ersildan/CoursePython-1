# объявление функции
def find_all(t, s):
    return [i for i in range(len(t)) if t[i] == s]

# считываем данные
t = input()
s = input()

# вызываем функцию
print(find_all(t, s))
