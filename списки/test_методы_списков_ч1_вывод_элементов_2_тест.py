    
n = int(input())               #  вводим кол-во чисел
lst = []                       #  создаем пустой список
for i in  range(n):            #  цикл длиой в кол-во чисел
    x = int(input())           #  вводим число
    print(x)                   #  выводим это число
    f = x  ** 2 + 2 * x + 1    #  считаем формулу с введенным числом
    lst.append(f)              #  добавляем результат в список

print()
    
print(*lst, sep='\n')          #  выводим список без квадратных скобок на каждой отдельной строке
    



