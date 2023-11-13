def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False


def get_next_prime(num):
    while is_prime(num+1) == False:
        num += 1
        continue
    return num + 1


num = int(input())
print(get_next_prime(num))
