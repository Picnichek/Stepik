def get_distance(x1, y1, x2, y2):
    return compute_hypotenuse(x1 - x2, y1 - y2)
def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


x1, y1 = float(input()), float(input())  # считываем координаты первой точки
x2, y2 = float(input()), float(input())  # считываем координаты второй точки

print(get_distance(x1, y1, x2, y2))      # вычисляем и выводим расстояние между точками

