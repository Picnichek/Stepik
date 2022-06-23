from random import *
print('Добро пожаловать в числовую угодайку')
x = randint(1, 100)


def is_valid(f):
    if f.isdigit():
        return True
    else:
        return False


y = is_valid(input('Введите число от 1 до 100 '))
if y == False:
    print('Я ведь просил ввести ЧИСЛО от 1 до 100',
          '\n', 'ладно, введи еще раз')
