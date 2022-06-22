s = input()

if s.count('f') == 0: 
    print('-2')
elif s.count('f') == 1: 
    print('-1')
else:
    s = s.replace('f', 'a', 1)   # меняем F на a до первого совпадения включительно
    print(s.find('f'))
