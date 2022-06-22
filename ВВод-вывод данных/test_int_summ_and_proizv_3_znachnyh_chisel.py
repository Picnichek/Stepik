
number = int(input())
a = ((number % 10 ** 3) // 10 **2)
b = ((number % 10 ** 2) // 10 **1)
c = ((number % 10 ** 1) // 10 **0)

print('Сумма цифр =', a + b + c, 'Произведение цифр =', a * b * c)
