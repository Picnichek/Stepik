
n = int(input())                    # вводим кол-во чисел
lst = []                            # создаем пустой список
for i in range(n):                  # задаем цикл длиной в кол-во чисел
    x = int(input())                # вводим число
    lst.append(x)                   # добавляем его в список
del lst [1::2]                      # удаляем каждое второе число начиная с 1 индекса тем самым удаляя нечетные индексы
print(lst)    
