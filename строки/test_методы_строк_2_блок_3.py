s = int(input()) 
count = 0                  # задаем счетчик количества числа 11 миним. 3 раза
for c in range(s):         # цикл длиной в строку
    x = input()            # вводим строку
    if x.count('11') >= 3: # если 11 встречается минимум 3 раза
        count += 1         # то добавляем 1 к счетчику
print(count)               # выводим счетчик
