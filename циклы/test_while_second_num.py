num = int(input())

while num > 100: # задаем цикл пока введенное число не станет двухзначным
    num % 10
    num = num // 10
print(num % 10)  # выводим последную цифру двухзначного числа
