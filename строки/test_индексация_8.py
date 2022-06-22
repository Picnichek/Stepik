s = input()

star = 0
plus = 0

for c in range(len(s)):
    if s[c] in ('*'):
        star += 1
    if s[c] in ('+'):
        plus += 1
        
print('Символ + встречается', plus, 'раз')
print('Символ * встречается' ,star, 'раз')