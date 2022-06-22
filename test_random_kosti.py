import random

again = 'd'
while again.lower() == 'd':

    print('бросаем кубики')
    print('значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('d - da n - net')
