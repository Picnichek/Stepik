weight = int(input())

if weight < 64:
    if weight < 60:
        print('Легкий вес')
    else:
        print('Первый полусредний вес')

else:
    if weight < 69:
        print('Полусредний вес')
    else:
        print('слишком тяжелый, весы заклинило! (о_О)')
