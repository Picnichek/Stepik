
s = input() #'192.168.0.3' #'192.168.0.300'  
s = s.split('.')                            # преобразуем строку в список
flag = 'ДА'                                 # вводим флаг равный "ДА" 
for i in range(len(s)):                     # цикл длиной в кол-во элементов списка
    s[i] = int(s[i])                        # преобразуем строку в число
    if s[i] < 0 or s[i] > 255:              # если значение итерации меньше 0 или значение итерации больше 255
        flag = 'НЕТ'                        # задаем флаг равный "НЕТ"
        break                               # останавливаем цикл
        
print(flag)                                 # выводим флаг

# другой вариант

# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')