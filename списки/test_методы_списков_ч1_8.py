n = int(input())                #  вводим кол-во строк
li = []                         #  вводим пустой список
for _ in range(n):              #  вводим цикл длиной в кол-во строк
    li.append(input())          #  добавляем введенную строку в список
index = int(input())            #  вводим индекс
res = ''                        #  вводим пустую строку
for s in li:                    #  цикл длиной в количество элементов
    if len(s) >= index:         #  если индекс цикла больше или равен введенному индексу то есть если в строке есть заданый индекс
        res += s[index - 1]     #  то добавляем значение введеного индекса минус 1
    
print(res)