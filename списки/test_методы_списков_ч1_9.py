
n = int(input())           # вводим кол-во строк
lst = []                   # создаем пустой список
for _ in range(n):         # задаем цикол равный кол-ву строк
    lst.extend(input())    # разбираем введеную строку на символы и расширяем список этими символами
print(lst)                 # выводим список