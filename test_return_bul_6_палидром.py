
def is_palindrome(text):
    lst = []
    text = text.lower()
    for i in range(len(text)):
        if text[i] not in '.,!?- ':
            lst.append(text[i])
    if lst[::] == lst[::-1]:
        return True
    else:
        return False

    pass

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))