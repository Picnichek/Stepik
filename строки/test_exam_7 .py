s = 'Python'#input()
total = ''
for c in range(len(s)):
    if c % 3 != 0:
        total += s[c]
print(total)

# s = input()                        другой вариант
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')
