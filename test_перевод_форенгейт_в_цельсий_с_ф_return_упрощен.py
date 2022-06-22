# функция перевода градусов Фаренгейта в градусы Цельсия упрощенный вариант
def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)

# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия