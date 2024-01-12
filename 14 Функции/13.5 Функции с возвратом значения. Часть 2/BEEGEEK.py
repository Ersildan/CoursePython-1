def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True


def is_even(num):
    return num % 2 == 0
    

# объявление функции
def is_valid_password(password):
    seq = password.split(":")
    
    if len(seq) == 3:
        seq = [int(el) for el in seq]
        a, b, c = seq[0], seq[1], seq[2]
        
        return is_palindrome(a) and is_prime(b) and is_even(c)
    
    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
