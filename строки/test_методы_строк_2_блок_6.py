s = input()                     # вводим строку   
count = 0                       # создаем счетчик кол-ва повторений
x = ''                          # создаем перем. той буквы, кот. повтор.
for c in range(len(s)):         # цикл равный длине введеной строки
    if s.count(s[c]) >= count:  # если буква индека встречается чаще чем текущая переменная
        count = s.count(s[c])   # то записываем это кол-во в пер. count
        x = s[c]                # приравниваем х этому символу
print(x)                        # выводим символ