import math

x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))

f = (x**5+(math.pow(math.cos(x**2),3))/(3.14*3.57*math.sin(y)+math.sqrt(x**7 - y**3)))

print('Значение f равно:' , f)

