import math

y = lambda a: 3 * a + 5 if a >= 0 else 3 * a - 5

a = float(input('Введите значение а: '))

xd = y(a)

print(f'Значение y ровно {xd}')
