# Нужно написать программу, которая выводит на экран количество 
# неотрицательных чисел последовательности и их произведение. 
# Если неотрицательных чисел нет, требуется вывести на экран «NO».
count = 0
p = 1                   # 1 ошибка p = 0
for i in range(1, 11):  # 2 ошибка range(1, 10)
    x = int(input())
    if x >= 0:          # 3 ошибка x > 0
        p = p * x
        count = count + 1
if count > 0:
    print(count)        # 4 ошибка print(x)
    print(p)
else:
    print('NO')