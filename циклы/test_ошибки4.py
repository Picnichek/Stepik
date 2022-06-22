# n = int(input())
# max_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit < max_digit:
#             digit = max_digit
#     n = n % 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)

n = int(input())
max_digit = -1                  # 0 кратен 3
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:   # последняя цифра должна быть больше максим. цифры
            max_digit = digit   # нужно максимальную приравнивать а не текущюю
    n = n // 10                 #  нужно удалить последнюю цифру
if max_digit == -1:             # неправильно задано условие
    print('NO')
else:
    print(max_digit)