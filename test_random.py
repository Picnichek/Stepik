import random
print(*[random.randint(1, 10) for _ in range(100)])

for _ in range(10):
    print(random.randint(1, 10), end=' ')
