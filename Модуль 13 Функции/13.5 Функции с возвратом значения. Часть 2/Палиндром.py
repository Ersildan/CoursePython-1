def is_palindrome(text):
    flag = False
    txt1 = txt.replace(".", "")
    txt2 = txt1.replace(",", "")
    txt3 = txt2.replace("!", "")
    txt4 = txt3.replace("-", "")
    txt5 = txt4.replace("?", "")
    txt6 = txt5.replace(" ", "")
    if txt6 == txt6[::-1]:
        flag = True
    else:
        return False
    return True


txt = input().lower()
print(is_palindrome(txt))
