# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False
    pass

def get_next_prime(num):
    while is_prime(num +1) == False:
        num += 1
    return num + 1

        
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))