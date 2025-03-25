import math

def area_of_quadrilateral(a, b, c, d, diagonal):
    # Полупериметр
    p = (a + b + c + d) / 2
    # Площадь по формуле Брахмагупты
    area = math.sqrt((p - a) * (p - b) * (p - c) * (p - d))
    return area

# Ввод длин сторон и диагонали
a = float(input("Введите длину первой стороны (a): "))
b = float(input("Введите длину второй стороны (b): "))
c = float(input("Введите длину третьей стороны (c): "))
d = float(input("Введите длину четвертой стороны (d): "))
diagonal = float(input("Введите длину диагонали: "))

# Вычисление площади
area = area_of_quadrilateral(a, b, c, d, diagonal)

print(f"Площадь выпуклого четырехугольника равна: {area:.2f}")
