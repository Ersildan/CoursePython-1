def is_password_good(password):
    total = 0
    if len(password) >= 8:
        total +=1
    if [a for a in password if a in '1234567890']: total +=1
    if password.lower() != password:
        total +=1
    if password.upper() != password:
        total +=1
    if total == 4:
        return True
    else:
        return False


password = input()
print(is_password_good(password))
