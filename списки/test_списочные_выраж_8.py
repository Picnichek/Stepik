s = print(*[i for i in input() if i in '0123456789'], sep='')  # выводим элементы если они являются числом

# [print(i, end = '') for i in input() if i.isdigit()] # isdigit другой вариант