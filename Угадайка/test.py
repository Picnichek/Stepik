from ast import While
from random import *
from time import process_time
print('Добро пожаловать в числовую угодайку')


def is_valid(f):

    if f.isdigit() and 0 < int(f):
        return int(f)

    else:
        return False


pass


def test(f):
    if f < x:
        f = 'Ваше число меньше загаданного, попробуйте еще разок'
    elif f > x:
        f = 'Ваше число больше загаданного, попробуйте еще разок'
    else:
        f = 'Вы угадали, поздравляем!'
    return f


pass


def communications():
    count = 0
    global right_line
    while True:
        count += 1
        print(f'Введите целое число от 1 до {right_line}')
        y = input()
        y = is_valid(y)
        if y == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        # if test(y) != 'Вы угадали, поздравляем!':
        #     continue
        else:
            x = test(y)
            print(x)
            if x == 'Вы угадали, поздравляем!':
                print('Количество попыток --', count)
                break


while True:
    again = input(
        'Начнем игру? "да" или "нет" ').lower()
    if again == 'да':
        right_line = input('задайте границу')
        right_line = is_valid(right_line)
        if right_line == False:
            print('Пожалуйста введите положительное число!!!')
        else:
            x = randint(1, right_line)
            communications()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
