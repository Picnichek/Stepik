num = int(input())
flag = 'YES'         # устанавливаем флаг = "ДА"
last = num % 10      # Берем последнюю цифру числа
while num:
    x = num % 10     # Берем последнюю цифру числа
    if x < last:     # если последняя цифра меньше нашей последней цифры 
        flag = 'NO'  # устанавливаем флаг = "НЕТ"
    else:            # если условие выше не выполняется
        last = x     # устанавливаем значение last = текущему значению последней цифры
                     # т.е. при вводе "2321" последняя = 1, и последняя в цикле тоже равна
                     # значит меням 1 на 1, потом 2 не меньше 1, значит меняем и ее        
                     # потом 3 не меньше 2, меняем и ее   но 2 меньше 3, значит меняем флаг на "НЕТ"     
    num = num // 10
print(flag)    
