# объявление функции
def convert_to_python_case(text):
    new_text = ""
    for el in text:
        if not el == el.lower():  # проверяем, что элемент в верхнем регистре (пропускаем цифры)
            new_text += "_" + el.lower()
        else:
            new_text += el
            
    return new_text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
