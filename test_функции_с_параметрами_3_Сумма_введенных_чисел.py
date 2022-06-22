# объявление функции
def print_digit_sum(num):
    list = [int(i) for i in str(num)] # создаем список из чисел 
    print(sum(list))                  # выводим сумму введенных элементов 
    pass

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)


# # объявление функции другой вариант
# def print_digit_sum(n):
#     c=0
#     while n!=0:
#         b=n%10
#         c+=b
#         n=n//10
#     print(c)

# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)