from math import sqrt
# объявление функции


def solve(a, b, c):
    d = b**2 - 4*(a*c)
    x_1 = 0
    x_2 = 0
    if d < 0:
        return'Корней нет', 'Корней нет'
    elif d == 0:
        return (-b/(2*a)), (-b/(2*a))
    else:
        x_1, x_2 = (-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
        return min(x_1, x_2), max(x_1, x_2)

    pass


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
