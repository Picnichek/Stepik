
colour_one = str(input())
colour_two = str(input())
red = 'красный'
blue = 'синий'
yellow = 'желтый'


if colour_one != red and colour_one != blue and colour_one != yellow:
    print('ошибка цвета')
elif colour_two != red and colour_two != blue and colour_two != yellow:
    print('ошибка цвета')


elif colour_one == red and colour_two == red:
    print(red)
elif colour_one == blue and colour_two == blue:
    print(blue)
elif colour_one == yellow and colour_two == yellow:
    print(yellow)

elif (colour_one == red and colour_two == blue) or (colour_one == blue and colour_two == red):
    print('фиолетовый')
elif (colour_one == red and colour_two == yellow) or (colour_one == yellow and colour_two == red):
    print('оранжевый')
elif (colour_one == blue and colour_two == yellow) or (colour_one == yellow and colour_two == blue):
    print('зеленый')






