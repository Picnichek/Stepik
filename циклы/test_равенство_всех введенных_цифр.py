num = int(input())

flag = 'YES'          # создаем флаг = "ДА"
last = num % 10       # выбираем последнюю цифру, которой должны равняться все остальные
while num: 
    x = num % 10      # выбираем последнюю цифру  
    if x != last:     # если она не равна last
        flag = 'NO'   # меняем значение флага на "НЕТ"     
    num = num // 10   # удаляем последнюю цифру
    
print(flag)  
