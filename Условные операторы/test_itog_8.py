one = int(input())
two = int(input())
three = int(input())
four = int(input())   
if ((one - two)^2 == (three - four)^2) or ((one + two)^2 == (four + three)^2):
    print('YES')
elif one == three or two == four:
    print('YES')
    
else:
    print('NO')     