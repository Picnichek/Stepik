num = int(input())         # Вводим число, допустим 192

while num > 9:             # цикл существует пока введ число больше 9
    total = 0              # задаем итоговую пременную
    while num > 0:         # подцикл сущ. пока число больше 0
        count = num % 10   # перебираем цифры числа справа налево  2 9 1
        total += count     # прибавляем к итогу каждую цифлу получим 12
        num //= 10         # удаляем последнюю цифру из введеного числа 192 19 1
    num = total            # приравниваем переменную num к total == 12
print(num)                 # выводим num тогда, когда новый num будет меньше 9