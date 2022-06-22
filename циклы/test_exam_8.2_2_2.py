# n = 7
# count = 0
# maximum = 1000
# for i in range(1, n + 1):
#     x = int(input())
#     if x // 4 == 0:
#         count += 1
#         if x < maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

n = 8                     # по условию 8 цифр а не 7
count = 0
maximum = -10 ** 12       # вроде ставят в 6 степени и работает, хз
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:        # перепутал целочисленное с остатком
        count += 1
        if x > maximum:   # знаки перепутал
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')