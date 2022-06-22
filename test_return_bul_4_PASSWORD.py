# объявление функции
def is_password_good(password):

    if len(password) < 8:
        return False
    else:
        flag1 = False 
        flag2 = False
        flag3 = False
        for i in range(len(password)):
            if password[i].isdigit():
                flag1 = True
            if password[i].isupper():
                flag2 = True 
            if password[i].islower():
                flag3 = True

        if (flag1 * flag2  * flag3) == 1:
            return True
        else:
            return False
    pass

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))