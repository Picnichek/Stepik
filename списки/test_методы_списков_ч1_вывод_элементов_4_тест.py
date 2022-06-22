
n = int(input())              
lst = []                       
for i in range(n):
    x = input()                # вводим строку
    if x not in lst :          # если этой строки еще нет в списке           
        lst.append(x)          # то добавялем ее в список

print(*lst, sep='\n')

