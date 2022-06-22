n = int(input())
num = 0
for i in range(1, n+1):
    if n % i == 0: # если введенное значение
                    # делится на i 
                    # то прибавляем к счетчику делитель i
        num += i
print(num)