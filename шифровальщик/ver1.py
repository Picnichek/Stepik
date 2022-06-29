print("Выберите язык: aнгл=e, рус=r")
lan = input()
print("Выберите шифрование: шифрование - ch, дешифрование - def")
chif = input()
print("Введите ключ шифрования (0) для дешифровки всех возможных вариантов")
n = int(input())
print("Введите фразу")
f = input()


def shifr(lang, chifr, key, fraze):
    if key == 0:
        for j in range(1, 25):
            word = ''
            for c in fraze:
                z = ord(c)
                if 1072 <= z <= 1103:
                    z += j
                    if z > 1103:
                        z -= 32
                if 1040 <= z <= 1071:
                    z += j
                    if z > 1071:
                        z -= 32
                if 97 <= z <= 122:
                    z += j
                    if z > 122:
                        z -= 26
                if 65 <= z <= 90:
                    z += j
                    if z > 90:
                        z -= 26
                word += chr(z)
            print(word)
        #print(chr(z), end='')


    elif lang == 'r':
        if chifr == 'ch':
            for c in fraze:
                z = ord(c)
                if 1072<=z<=1103:
                    z += key
                    if z >1103:
                        z-=32
                if 1040<=z<=1071:
                    z += key
                    if z >1071:
                        z-=32
                print(chr(z), end='')
        if chifr == 'def':
            for c in fraze:
                z = ord(c)
                if 1072<=z<=1103:
                    z-=key
                    if z <1072:
                        z+=32
                if 1040<=z<=1071:
                    z-=key
                    if z <1040:
                        z+=32
                print(chr(z), end='')
    elif lang == 'e':
        if chifr == 'ch':
            for c in fraze:
                z = ord(c)
                if 97<=z<=122:
                    z += key
                    if z >122:
                        z-=26
                if 65<=z<=90:
                    z += key
                    if z >90:
                        z-=26
                print(chr(z), end='')
        if chifr == 'def':
            for c in fraze:
                z = ord(c)
                if 97<=z<=122:
                    z-=key
                    if z <97:
                        z+=26
                if 65<=z<=90:
                    z-=key
                    if z <65:
                        z+=26
                print(chr(z), end='')
        pass

shifr(lan, chif, n, f)

# fraze = 'абв'  # 'Hawnj pk swhg xabkna ukq nqj.'
# for j in range(25):
#     word = ''
#     for c in fraze:
            
#         z = ord(c)
#         if 1072 <= z <= 1103:
#             z += j
#             if z > 1103:
#                 z -= 32
#         if 1040 <= z <= 1071:
#             z += j
#             if z > 1071:
#                 z -= 32
#         word += chr(z)
#     print(word)
#         #print(chr(z), end='')
