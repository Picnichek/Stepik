
n = [i for i in input().split('-')]
n1 = ''.join(n)
if n1.isdigit():
    n1 =True
else:
    print('NO')
    
if n1 == True:
    if n[0] == '7':
        del n[0]
    if len(n[0]) == 3 and len(n[1]) == 3 and len(n[2]) == 4:
        print('YES')
    else:
        print('NO')
# другой вариант
# n = input().split("-")
# c = [len(i) for i in n] 
# if c == [3, 3, 4] and ''.join(n).isdigit(): 
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7': 
#     print("YES")
# else:
#     print("NO")