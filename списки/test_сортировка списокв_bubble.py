import time
start_time = time.time()
a = [1,2,3, 10,5 ,4, 11, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 11, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4, 1,2,3, 10,5 ,4 ]
n = len(a)
for i in range(n-1):
    flag = False
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j +1], a[j]
            flag = True
        else:
            flag = False


    if flag == False:
        break
print(a)
print('--- %s seconds ---' % (time.time() -start_time))