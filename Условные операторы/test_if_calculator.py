number_one = int(input())
number_two = int(input())
operation = str(input())

if operation == '+':
    print(number_one + number_two)
elif operation == '-':
    print(number_one - number_two)
elif operation == '*':
    print(number_one * number_two)
elif operation == '/':
    if number_two == 0:
        print('На ноль делить нельзя!')
    else:
        print(number_one / number_two)
else:
    print('Неверная операция')
