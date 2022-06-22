largest = int(input())  # принимаем первое число за максимальное
for i in range(9):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)