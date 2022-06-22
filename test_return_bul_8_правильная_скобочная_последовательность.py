# объявление функции
def is_correct_bracket(text):
    count = 0
    if text[-1] == '(' or text[0] == ')':
        return False
    for i in range(len(text)):
        if text[i] == ')' and count == 0:
            return False
        elif text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
    if count == 0:
        return True
    else:
        return False
    pass

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))