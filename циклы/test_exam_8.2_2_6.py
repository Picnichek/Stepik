n = int(input())
count_3 = 0
last_number = n % 10
count_last_number = 0
count_chet = 0
summa_bolee_5 = 0
proizv_bolee_7 = 1
vstrech_5 = 0

while n:
    x = n % 10
    if x == last_number:
        count_last_number += 1
    if x == 3:
        count_3 += 1
    if x % 2 == 0:
        count_chet += 1
    if x > 5:
        summa_bolee_5 += x
    if x > 7:
        proizv_bolee_7 *= x
    if x == 0 or x == 5:
        vstrech_5 += 1
    n //= 10
print(count_3)    
print(count_last_number)
print(count_chet)
print(summa_bolee_5)
print(proizv_bolee_7)
print(vstrech_5)