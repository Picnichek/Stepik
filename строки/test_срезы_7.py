s = input()   

print(s[2])           # 3й символ строки
print(s[-2])          # предпоследний символ
print(s[:5])          # первые 5 символов
print(s[:len(s) -2])  # вся строка без 2х последних символов
# верхнюю строку можно записать как print(s[:-2])
print(s[::2])         # все символы с четными индексами
print(s[1::2])        # все символы с нечетными индексами
print(s[::-1])        # все символы в обратном порядке
print(s[::-2])        # все символы через один начиная с последнего