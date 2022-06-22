w1 = int(input())
total = 0
while w1 >= 25:
    total += 1
    w1 -= 25
while w1 >= 10:
    total += 1
    w1 -= 10
while w1 >= 5:
    total += 1
    w1 -= 5
while w1 >= 1:
    total += 1
    w1 -= 1

print(total)
