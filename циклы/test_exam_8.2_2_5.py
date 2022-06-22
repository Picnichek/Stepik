n = int(input())
while n // 100 != 0:
    x = n % 10
    n //= 10
print(x)