# x = int(input())
# for i in range(x):
#     print('*' * 19)
n = int(input())

for j in range(1, n + 1):
    if j == 1 or j == n:
        print('*' * 19)
    if 1 < j < n:
        print('*' + ' ' * 17 + '*' )           
