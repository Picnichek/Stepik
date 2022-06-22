
number = int(input())
if number < 0 or number > 36:
    print('ошибка ввода')
if number == 0:
    print('зеленый')
if number >= 1 and number <= 10:
    if number % 2 == 0:
        print('черный')
    else:
        print('красный')
if number >= 11 and number <= 18:
    if number % 2 == 0:
        print('красный')
    else:
        print('черный')
if number >= 19 and number <= 28:
    if number % 2 == 0:
        print('черный')
    else:
        print('красный')
if number >= 29 and number <= 36:
    if number % 2 == 0:
        print('красный')
    else:
        print('черный')
