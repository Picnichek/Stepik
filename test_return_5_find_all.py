# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return lst
    pass

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

# объявление функции
#def find_all(target, symbol):
    #return [x for x in range(len(target)) if target[x] == symbol]

# считываем данные
#s = input()
#char = input()

# вызываем функцию
#print(find_all(s, char))