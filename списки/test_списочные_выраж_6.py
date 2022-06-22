
n = input().split(' ')             # вводим строку из чисел
t = [int(i) ** 3 for i in n ]      # число цикла возводим в куб
for i in t:      
    print(i, end=' ')
