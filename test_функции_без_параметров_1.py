# объявление функции
def draw_box():
    for _ in range(1):
        print('*' * 10)
    for _ in range(12):
        print('*', ' ' * 8, '*', sep=""  )
    for _ in range(1):
        print('*' * 10)
    pass

# основная программа
draw_box()  # вызов функции