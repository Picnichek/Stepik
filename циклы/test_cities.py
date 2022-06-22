city1 = input()
city2 = input()
city3 = input()

lencity1 = len(city1)
lencity2 = len(city2)
lencity3 = len(city3)

if lencity2 > lencity1 < lencity3:
    print(city1)
elif lencity1 > lencity2 < lencity3:
    print(city2)
else:
    print(city3)

if lencity2 < lencity1 > lencity3:
    print(city1)
elif lencity1 < lencity2 > lencity3:
    print(city2)
else:
    print(city3)
