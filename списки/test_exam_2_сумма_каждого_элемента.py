first = [int(i) for i in input().split()]  # создаем список элементов в числовом формате
second = [int(i) for i in input().split()] # создаем список элементов в числовом формате
total = []                                 # пустой список
for i in range(len(first)):                # цикл длиной в количество элементов списка
    total.append(first[i] + second[i])     # добавляем в тотал сумму элементов
print(*total)

# другой вариант

# l, m = input().split(), input().split()
# print(*(int(l[i]) + int(m[i]) for i in range(len(l))))