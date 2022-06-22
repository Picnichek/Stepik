
s = input().lower().split() # вводим строку заранее переводя ее в нижний регистр
count1 = s.count('a') # находим количество нужных артиклей суммируем и выводим
count2 = s.count('an')
count3 = s.count('the')
total = count1 + count2 + count3
print('Общее количество артиклей:', total )