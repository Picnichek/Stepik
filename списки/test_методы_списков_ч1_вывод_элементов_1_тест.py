numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0                                                         # создаем итоговую переменную
for i in range(len(numbers)):                                     # цикл длиной в кол-во элементов в numbers
    x = numbers[i] ** 2                                           # вводим переменную которая равна текущему элементу в квадрате
    total += x                                                    # прибавляем эту переменную в итоговую
print(total)
    




