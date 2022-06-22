num = int(input())            # вводим число                   
total = 0                     # переменная суммы факториалов
for i in range(1, num + 1):
    count = 1
    for j in range(1, i + 1):
        count *= j
    total += count
print(total)
