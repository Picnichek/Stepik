a = int(input())
b = int(input())
summ_count = 0                 # максимальная сумма делителей
max_x = 0                      # макс значение у кот-го сумма делителей будет наибольшей     

for x in range(a, b + 1):      # цикл проверки чисел a и b  
    count = 0                  # счетчик делителей  
    for i in range(1, x + 1):  # цикл для проверки диапазона чисел
        if x % i == 0:         # если остаток от деления цикла x на цикл i = 0 
            count += i         # прибавляем к счетчику делителей 1 
        if count >= summ_count:# если счетчик больше макс суммы делителей
            summ_count = count # макс сум дел =счетчику
            max_x = x          # макс знач у кот-го сумма дел наиб = циклу x
print(max_x, summ_count)       # выводим макс значение и макс сумму  

            
            