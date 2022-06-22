
num = int(input())
total = 0               # создана для нахожд. суммы всех цифр
count = 0               # для нахожд. кол-ва цифр
proizv = 1              # для нахожд. произведения цифр
sred_arif = 0           # среднее арифмитическое = сумма цифр / кол-во цифр
first_num = num % 10    # первая(а точнее последняя цифра) из введенного числа

while num:
    x = num % 10        # создаем для нахождения последней цифры
    total = total + x   # сумма = последняя цифра + total 
    count = count + 1   # кол-во цифр каждый цикл прибавляем 1 к count = 0
    proizv = proizv * x # умножаем каждую цифру на предыдущюю
    sred_arif = total / count # сред. ариф. 
    num = num // 10     # удаляем из введенного числа последнюю цифру
print(total)
print(count)
print(proizv)           # выводим требуемые итоги
print(sred_arif)
print(x)
print(first_num + x)
