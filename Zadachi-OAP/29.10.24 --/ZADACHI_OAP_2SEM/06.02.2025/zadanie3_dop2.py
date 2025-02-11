import math

X = (int(input("Введите координату X1: ")), int(input("Введите координату Y1: ")), int(input("Введите координату Z1: ")))
Y = (int(input("Введите координату X2: ")), int(input("Введите координату Y2: ")), int(input("Введите координату Z2: "))) 
Z = (int(input("Введите координату X3: ")), int(input("Введите координату Y3: ")), int(input("Введите координату Z3: ")))
T = (int(input("Введите координату X4: ")), int(input("Введите координату Y4: ")), int(input("Введите координату Z4: ")))

points = [X, Y, Z, T]
min_distance = float('inf') # Значение в бесконечность =)

for i in range(len(points)): # инициализирование точек в пространстве (цикл)
    for j in range(i+1, len(points)):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) # Формула решения дистанции
        if dist < min_distance:
            min_distance = dist
            min_points = (points[i], points[j])
        else:
            print('Error')
            
print("Минимальное расстояние:", min_distance)
print("Точки:", min_points)
