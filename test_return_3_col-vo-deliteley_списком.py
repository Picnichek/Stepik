# объявление функции
def get_factors(num):
    d = []
    for i in range(1, num + 1):
        if num % i == 0:
            d.append(i)

    return d
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


#def get_factors(num):
    #return [n for n in range(1, num + 1) if num % n == 0]


#n = int(input())
#print(get_factors(n))