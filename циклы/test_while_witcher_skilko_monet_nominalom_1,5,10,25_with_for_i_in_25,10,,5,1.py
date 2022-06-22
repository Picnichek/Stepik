w1 = int(input())
total = 0
for i in (25, 10, 5, 1):
    while w1 // i > 0:
        total += 1
        w1 -= i
print(total)
