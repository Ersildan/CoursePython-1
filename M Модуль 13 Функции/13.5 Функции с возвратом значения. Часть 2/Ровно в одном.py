def is_one_away(word1, word2):
    flag1 = False
    flag2 = False
    total = 0
    if len(txt1) == len(txt2):
        flag1 = True
    for i in range(len(txt1)):
        if txt1 [i] != txt2 [i]:
            total +=1
    if total == 1:
        flag2 = True
    else:
        return False
    return True


txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))
