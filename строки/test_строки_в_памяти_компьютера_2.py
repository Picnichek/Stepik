# s = input()             

# for c in range(len(s)):           # задаем длину цикла равный количеству введенных символов
#     print(ord(s[c]), end = ' ')   # выводим код таблицы символов Unicode каждого введенного символа

s = input()
for c in s:
    print(ord(c), end=' ')