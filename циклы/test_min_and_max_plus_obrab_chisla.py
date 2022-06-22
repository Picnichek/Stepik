a = int(input())
first = a // 100
second = (a % 100) // 10
third = a % 10
sred = (first + second + third) - max(first, second, third) - min(first, second, third)
if sred == max(first, second, third) - min(first, second, third):
    print('Число интересное')
else:
    print('Число неинтересное')