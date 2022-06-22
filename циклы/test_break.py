n = int(input())
for i in range(2, n+1): # задаем отчет от 2 до n включительно
    if n % i == 0:      # если n делится на i без остатка то печатаем i
        print(i)
        break
