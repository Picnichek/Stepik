num = int(input())            # вводим число менше 10
for i in range (num):         # задаем длину до введенного числа  
    for j in range(3):        # задаем длину 3 т.к. в строке будет 3 столбца
        print(num, end = ' ') # выводим введенное число с пробелом 3 раза
    print()                   # это как энтер  