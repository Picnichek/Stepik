

def is_valid_password(password):
    check = 0
    count = 0
    pal = []
    simple = []
    chet = []
    if len(password) != 3:
        return False
    else:
        pal = password[0]
        simple = int(password[1])
        chet = int(password[2])
        if pal[::] == pal[::-1]:
            check += 1
        for i in range(1, simple + 1):
            if simple % i == 0:
                count += 1
        if count == 2:
            check += 1
        if chet % 2 == 0:
            check += 1
 
        if check == 3:
            return True
        else:
            return False
    
                   
    
    pass

# считываем данные
psw = input().split(':')

# вызываем функцию
print(is_valid_password(psw))