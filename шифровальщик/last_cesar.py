eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
fraze = input().split()
total =''
for c in fraze:
    count = 0
    for j in c:
        if j.isalpha():
            count +=1
    for k in c:
        if k.isalpha():
            if k in eng_upper_alphabet:
                x = eng_upper_alphabet.index(k) + count
                if x > 25:
                    x-=26
                total += eng_upper_alphabet[x]
            elif k in eng_lower_alphabet:
                x = eng_lower_alphabet.index(k) + count
                if x > 25:
                    x-=26
                total += eng_lower_alphabet[x]
            elif k in rus_lower_alphabet:
                x = rus_lower_alphabet.index(k) + count
                if x > 31:
                    x-=32
                total += rus_lower_alphabet[x]
            elif k in rus_upper_alphabet:
                x = rus_upper_alphabet.index(k) + count
                if x > 31:
                    x-=32
                total += rus_upper_alphabet[x]             
        else:
            total+=k
    total+=' '    
print(total)



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