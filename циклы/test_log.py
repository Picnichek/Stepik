import math
n = int(input())
num = 0
for i in range(1, n + 1):
    num += i ** (-1)
    num2 = num - math.log(n)
print(num2)
        