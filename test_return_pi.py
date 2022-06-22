import math
# объявление функции
def get_circle(radius):
    return 2 * math.pi * radius, math.pi*r**2
    pass

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)