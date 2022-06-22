from math import factorial   # выбираем из math факториал
num = int(input())           # вводим цифру
total = 0                    # задаем сумму факториалов
for i in range (1, num + 1): # задаем цикл от 1 до num включительно
    count = factorial(i)     # задаем счетчик равынй факториалу i 
    total += count           # суммируем полученный факториал с суммой факториалов
    
print(total)                 # выводим сумму факториалов