def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

print(compute_hypotenuse(3, 4))
print(compute_hypotenuse(5, 12))
print(compute_hypotenuse(1, 1))

# если нужно ввести данные
x = int(input())
y = int(input())

hypotenuse = compute_hypotenuse(x, y)

print(hypotenuse)