x = int(input())
y = int(input())
total = 0
for i in range(x, y + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1
print(total)