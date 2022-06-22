# n = input()
# product = n % 10
# while n >= 10:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

n = int(input())                # неправильно выбран тип данных
product = 1                     # неправильно выбрано значение при умн. 1
while n:                        # неправильно выбран цикл нужен пока n > 0 или пока есть цифра
    digit = n % 10
    #product = product * digit   # можно еще упростить на product *= digit
    product *= digit
    n //= 10
print(product)