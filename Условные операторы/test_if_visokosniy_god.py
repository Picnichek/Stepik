first = int(input())

if (first % 4 == 0 and first % 100 != 0) or first % 400 == 0:
    print('YES')
else:
    print('NO')
