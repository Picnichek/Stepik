

s = input().split()
for i in range(len(s)):
    print(s[i][1:] + s[i][0] + 'ки', end=(' '))


# print(*[i[1:] + i[0] + "ки"for i in input().split()])  # другой вариант в 1 строку

