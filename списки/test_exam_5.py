
# n = [int(i) for i in input().split()] #  создаем список и преобразуем в числа
# print(*n, sep=('+'), end=('='))       # выводим элементы списка через разделитель "+" и "=" на конце строки и добавляем сумму элементов
# print(sum(n)) 

# if n[0] == 7 and len(n[1] == 3) and len(n[2] == 3) and len(n[3] == 4) or len(n[0] == 3)  and len(n[1] == 3) and len(n[2] == 4):
#     print('YES')
# else:
#     print('NO')

# n = [i for i in input().split('-')]
# print(n)
# n1 = ''.join(n)
# print(n1)
# if n1.isdigit():
#     n1 =True
# else:
#     print('NO')
#     quit()
# if n[0] == '7' and len(n[1] == '3'):
#     print('YES')

s = input().split()
longest = 0

for c in range(len(s)):
    if len(s[c]) > longest:
        longest = len(s[c])


print(longest)

# print(max([len(a) for a in input().split()]))  # другой вариант в 1 строку

