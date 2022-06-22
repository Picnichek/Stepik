one = int(input())
two = int(input())
three = int(input())
four = int(input())   
if ((one + two + three + four % 2 !=0) and (one != three) and (two != four)
    and ((one - three)**2 + (two - four)**2 == 5)):
    print('YES') 
else:
    print('NO')        