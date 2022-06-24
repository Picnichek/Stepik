from lib2to3.pygram import Symbols
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'

chars = digits + lowercase_letters + uppercase_letters + punctuation

cntpw = int(input('укажите количество паролей для генерации'))
lenpw = int(input('напишите количество символов в пароле'))
dig = input('Включать ли цифры "0123456789" (да/нет)?')
uppw = input(
    'Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (да/нет)?')
lowpw = input(
    'Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz" (да/нет)?')
symbols = input('Включать ли символы "!#$%&*+-=?@^_"(да/нет)?')
unsymb = input('Исключать ли неоднозначные символы il1Lo0O (да/нет)?')


def genpw():
    symb = []
    total = []
    if dig == 'да':
        symb.append(digits)
    if uppw == 'да':
        symb.append(uppercase_letters)
    if lowpw == 'да':
        symb.append(lowercase_letters)
    if symbols == 'да':
        symb.append(punctuation)
    for x in symb:
        for y in list(x):
            total.append(y)
    if unsymb == 'да':
        total.remove('i')
        total.remove('l')
        total.remove('1')
        total.remove('L')
        total.remove('o')
        total.remove('0')
        total.remove('O')
    for _ in range(cntpw):
        lst = []
        for _ in range(lenpw):
            lst.append(random.choice(total))
        # print(''.join(lst))
        print(''.join(lst))


genpw()
