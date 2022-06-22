     
n = int(input())  
otric = []
zero = []
poloj = []
for i in range(n):       # цикл длиной в введеное число
    x = int(input())     # вводим цифру
    if x < 0:            # если она меньше 0
        otric.append(x)  # добавляем ее в отриц список
    if x == 0:           # если она равна нулю
        zero.append(x)   # добавляем ее в нулевой список
    if x > 0:            # если больше нуля
        poloj.append(x)  # добавляем в полож список
print(*otric, sep='\n')  # выводим каждый список без скобок с переходом на новую строку
print(*zero, sep='\n')
print(*poloj, sep='\n')
        
        
    
    
