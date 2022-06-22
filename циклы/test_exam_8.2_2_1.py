# n = int(input())
# s = 0
# while n > 10:
#     if n % 2 == 1:
#         s = n % 10
#     n //= 10
# print(s)

n = int(input())
s = 0
while n:
    x = n % 10
    if x % 2 == 0:
        s += x
    n //= 10
print(s)