
s = input().split()      # вводим строку и разбиваем ее на список          
lst = []                 # создаем пустой список
for i in range(len(s)):  # цикл длиной в кол-во элементов списка
    s[i] = int(s[i])     # преобразуем значение итерации в число и записываем в пустой список
    
    lst.append(s[i])

maximum = lst.index(max(lst))  # находим индекс максимального элемента списка
minimum = lst.index(min(lst))  # находим индекс минимального элемента списка
lst[maximum], lst[minimum] = lst[minimum], lst[maximum]   # меняем их местами
print(*lst)     # выводим получившийся список
# print(maximum)
# print(minimum)
# print(lst.index(maximum))
# print(lst.index(minimum))

