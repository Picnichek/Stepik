num = int(input())
flag = 'YES'
while num //10 !=0: # считаем до предпоследней цифры
    x = num % 10
    num = num // 10
    if x > num:
        flag = 'NO'
print(flag)