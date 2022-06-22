# n = int(input())
# while n > 0:
#     n %= 10
# print(n)

n = int(input())
while n > 9:    # если n > 0 то получим младшую цифру
    n //= 10    # нужно отбрасывать последнюю цифру
print(n)