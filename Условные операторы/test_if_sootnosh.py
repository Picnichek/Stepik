number = int(input())
if number // 10 ** 3 + number % 10 == number %10 ** 3 // 10 ** 2 - number % 10 ** 2 // 10:
    print('ДА')
else:
    print('НЕТ')
