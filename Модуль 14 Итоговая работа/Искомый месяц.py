def get_month(language, number):
    ru = ['lol','январь', 'февраль',' март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en = ['lol','january', 'february', 'march', 'april',' may',' june', 'july', 'august',' september', 'october', 'november', 'december']
    if lan == 'ru':
        print(ru[num])
    else:
        print(en[num])


lan = input()
num = int(input())
get_month(lan, num)
