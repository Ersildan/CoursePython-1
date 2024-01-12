def is_pangram(text):
    flag = False
    a = text.replace(" ", "")
    b = set(a)
    if len(b) == 26:
        flag = True
    return flag    


text = input().lower()
print(is_pangram(text))
