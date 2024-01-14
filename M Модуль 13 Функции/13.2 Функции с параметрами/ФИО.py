def print_fio(name, sur, pat):
    print(name[0], sur[0], pat[0], sep='')
    
# считываем данные
name, sur, pat = input().title(), input().title(), input().title()

# вызываем функцию
print_fio(sur,name, pat)
