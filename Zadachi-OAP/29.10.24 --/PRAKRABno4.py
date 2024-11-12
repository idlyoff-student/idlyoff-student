import math

radius = float(input("Введите радиус круга: "))

if radius <= 0:
    print("Расчет невозможен")
else:
    area = math.pi * (radius ** 2)
    print(f"Площадь круга с радиусом {radius} равна {area:.2f}")
