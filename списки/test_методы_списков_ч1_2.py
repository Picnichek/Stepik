count = int(input())     # вводим кол-во слов 
lst = []                 # создаем пустой список
 
for c in range(count):   # задаем цикл длиной в кол-во слов
    lst.append(input())  # добавляем введенные данные в список

print(lst)               # выводим список
