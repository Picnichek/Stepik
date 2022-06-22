import time
start_time = time.time()
a = [3, 2, 1, 3, -1,]
n = len(a)
lst = []


for i in range(n):
    lst.append(min(a))
    a.remove(min(a))


print(lst)
print('--- %s seconds ---' % (time.time() - start_time))


