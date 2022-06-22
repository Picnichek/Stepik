rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
green = rainbow.index('Green')                                               # находим индекс зеленого
violet = rainbow.index('Violet')                                             # находим индекс фиолетового
rainbow[green] = 'Зеленый'                                                   # меняем грин на зеленый
rainbow[violet] = 'Фиолетовый'                                               # меняем виолет на фиолетовый

print(rainbow)




# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)