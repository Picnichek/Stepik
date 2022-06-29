
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def chru(chifr, key, lng, fraza):
    total = ''
    if chifr =='ch':
        if lng == 'ru':
            for c in range(len(fraza)):
                if fraza[c] in rus_lower_alphabet:
                    x = rus_lower_alphabet.index(fraza[c]) + key
                    if x > 31:
                        x-=32
                    total +=rus_lower_alphabet[x]
                elif fraza[c] in rus_upper_alphabet:
                    x = rus_upper_alphabet.index(fraza[c]) + key
                    if x > 31:
                        x-= 32
                    total += rus_upper_alphabet[x]
                else:
                    total+=fraza[c]
        elif lng =='en':
            for c in range(len(fraza)):
                if fraza[c] in eng_lower_alphabet:
                    x = eng_lower_alphabet.index(fraza[c]) + key
                    if x > 25:
                        x-=26
                    total +=eng_lower_alphabet[x]
                elif fraza[c] in eng_upper_alphabet:
                    x = eng_upper_alphabet.index(fraza[c]) + key
                    if x > 25:
                        x-= 26
                    total += eng_upper_alphabet[x]
                else:
                    total+=fraza[c]
    elif chifr == 'def':
        if lng == 'ru':
            for c in range(len(fraza)):
                if fraza[c] in rus_lower_alphabet:
                    x = rus_lower_alphabet.index(fraza[c]) - key
                    total +=rus_lower_alphabet[x]
                elif fraza[c] in rus_upper_alphabet:
                    x = rus_upper_alphabet.index(fraza[c]) - key
                    total += rus_upper_alphabet[x]
                else:
                    total+=fraza[c]
        elif lng =='en':
            for c in range(len(fraza)):
                if fraza[c] in eng_lower_alphabet:
                    x = eng_lower_alphabet.index(fraza[c]) - key
                    total +=eng_lower_alphabet[x]
                elif fraza[c] in eng_upper_alphabet:
                    x = eng_upper_alphabet.index(fraza[c]) - key
                    total += eng_upper_alphabet[x]
                else:
                    total+=fraza[c]

    print(total, end='')



    pass

def podbor(fraza):
    for j in range(count):
        total = ''
        for c in range(len(fraza)):
            if fraza[c] in rus_lower_alphabet:
                x = rus_lower_alphabet.index(fraza[c]) - j
                # if x > 31:
                #     x -=32 
                total += rus_lower_alphabet[x]
            elif fraza[c] in rus_upper_alphabet:
                x = rus_upper_alphabet.index(fraza[c]) - j
                # if x > 31:
                #     x-= 32
                total += rus_upper_alphabet[x]
            elif fraza[c] in eng_lower_alphabet:
                x = eng_lower_alphabet.index(fraza[c]) - j
                # if x > 25:
                #     x-= 26
                total += eng_lower_alphabet[x]
            elif fraza[c] in eng_upper_alphabet:
                x = eng_upper_alphabet.index(fraza[c]) - j
                # if x > 25:
                #     x-= 26
                total+= eng_upper_alphabet[x]
            else:
                total+=fraza[c]
        print(total)


    pass

print('введите "да" для запуска программы с известным ключом и "нет" для дешифровки')
proc= input()
if proc =='да':
    print("Выберите язык: aнгл=en, рус=ru")
    lan = input()
    print("Выберите шифрование: шифрование - ch, дешифрование - def")
    chif = input()
    print("Введите ключ шифрования, введите")
    n = int(input())
    print("Введите фразу")
    f = input()
    chru(chif, n, lan, f)
elif proc =='нет':
    print('введите язык дешифровки "ru", "en"')
    lang = input()
    print('Введите фразу для дешифровки ')
    x = input()
    if lang =='ru':
        count = 32
    elif lang == 'en':
        count = 26
    podbor(x)

# fraza = 'я.б,в,АБ,Вabc,zABC,Z'
# key = int(input())
# total = ''
# for c in range(len(fraza)):
    
#     if fraza[c] in rus_lower_alphabet:
#         x = rus_lower_alphabet.index(fraza[c]) + key
#         if x > 31:
#             x -=32 
#         total += rus_lower_alphabet[x]
#     elif fraza[c] in rus_upper_alphabet:
#         x = rus_upper_alphabet.index(fraza[c]) + key
#         if x > 31:
#             x-= 32
#         total += rus_upper_alphabet[x]
#     elif fraza[c] in eng_lower_alphabet:
#         x = eng_lower_alphabet.index(fraza[c]) + key
#         if x > 25:
#             x-= 26
#         total += eng_lower_alphabet[x]
#     elif fraza[c] in eng_upper_alphabet:
#         x = eng_upper_alphabet.index(fraza[c]) + key
#         if x > 25:
#             x-= 26
#         total+= eng_upper_alphabet[x]
#     else:
#         total+=fraza[c]
# print(total, end='')
