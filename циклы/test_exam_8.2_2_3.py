# n = 4
# count = 0
# maximum = 999
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = i
#             break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


n = 4
count = 0
maximum = - 10 ** 4       # неверно задан  
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x    # неверно присваивается значение
            #break         # не нужно прерывание цикла
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')