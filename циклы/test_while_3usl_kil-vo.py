w1 = input()
total = 0
while w1 not in ('стоп', 'хватит', 'достаточно'):
    total += 1
    w1 = input()
print(total)
