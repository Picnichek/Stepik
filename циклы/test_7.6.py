num = 1
for i in range(1, 11):
    n = int(input())
    if n != 0:   
        num *= n # умножаем счетчик на введенную цифру 
                    # и присваиваем переменной
print(num)