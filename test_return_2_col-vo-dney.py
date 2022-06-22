# объявление функции
def get_days(month):
    if month in (4,6,9,11):
        return 30
    elif month == 2:
        return  28
    elif month in (1,3,5,7,8,10,12):
        return 31
    else:
        return 'введено число больше 12'
    pass

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

# объявление функции
#def get_days(month):
 #   m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #  return m[month - 1]
# считываем данные
#num = int(input())
#
# вызываем функцию
#print(get_days(num))