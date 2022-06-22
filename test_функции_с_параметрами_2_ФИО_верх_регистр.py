# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].capitalize(), name[0].capitalize(), patronymic[0].capitalize(), sep='')
    
    pass

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)


