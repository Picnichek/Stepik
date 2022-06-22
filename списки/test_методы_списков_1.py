# numbers = [8, 9, 10, 11]
# print(numbers)
# numbers[1] = 17
# print(numbers)
# numbers2 = [4, 5, 6]
# numbers.extend(numbers2)
# print(numbers)
# del numbers[0]
# print(numbers)
# numbers.extend(numbers)
# print(numbers)
# numbers.insert(3, 25)
# print(numbers)


numbers = [8, 9, 10, 11]    # исходный список

numbers[1] = 17             # меняем второй элемент списка на 17           

numbers2 = [4, 5, 6]        # создаем второй список 
numbers.extend(numbers2)    # расширяем первый список вторым   

del numbers[0]              # удаляем 1й элемент

numbers.extend(numbers)     # удваиваем список путем расширения    

numbers.insert(3, 25)       # вставляем элемент в спискок по индексу 3 на 25          
print(numbers)              #  выводим список