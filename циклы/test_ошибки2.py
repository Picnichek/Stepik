# Нужно написать программу, которая выводит на экран сумму всех отрицательных 
# чисел последовательности и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO».

mx = -10 **6                 # 4 ошибка mx = 0
s = 0
for i in range(1, 11):     # 2 ошибка range(11)
    x = int(input())
    if x < 0:
        s += x          # 1 ошибка s = x
        if x > mx:# 3 ошибка x > mx
            mx = x
if s < 0:              # 5 ошибка без условия    print(s) print(mx)
    print(s)
    print(mx)
else:
    print('NO')
    
    
    


# mx = 0
# s = 0
# for i in range(11):
#     x = int(input())
#     if x < 0:
#         s = x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)