n = int(input())
largest = 0
prelargest = 0
for i in range(1, n + 1):
    x = int(input())
    if x > largest:          # если x больше переменной largest
        prelargest = largest #  присваиваем prelargest к largest
        largest = x          # а largest приравниваем к x
    elif x > prelargest:     # если x больше prelargest
        prelargest = x       # присваиваем prelargest к x

print(largest)
print(prelargest)
