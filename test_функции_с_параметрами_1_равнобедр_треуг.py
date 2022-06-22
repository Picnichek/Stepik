# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):    # цикл от 1 до половины включительно 
        print(fill * i)
    for i in range(base // 2 , 0, -1):   # цикл от половины не включительно до нуля с шагом -1
        print(fill * i)

    pass

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

# # объявление функции  другой вариант
# def draw_triangle(fill, base):
#     print(*[fill * (min(i, base + 1 - i)) for i in range(1, base + 1)], sep="\n")

# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)