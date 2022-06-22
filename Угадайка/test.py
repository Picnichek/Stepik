
from enum import Flag
from random import *
x = randint(1, 10)
while True:
    y = int(input('угадайте загаданное число от 1 до 100!!!'))
    if y < x:
        print('Слишком мало, попробуйте еще раз')
    elif y > x:
        print('Слишком много, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break
print('загаданное число - ', x)
