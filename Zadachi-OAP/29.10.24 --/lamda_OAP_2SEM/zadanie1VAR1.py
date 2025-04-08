import math

def y(a,b,x):
  calc = abs(x) + 3 * a / (math.cos(b) + math.sqrt(a))
  return calc

a = float(input('Введите а: '))
b = float(input('Введите b: '))
x = float(input('Введите x: '))

result = y(a,b,x)

print(f'Значение Y ровно {result}')


#import math

#y = lambda a, b, x: abs(x) + 3 * a / (math.cos(b) + math.sqrt(a))

#a = float(input('Введите а: '))
#b = float(input('Введите b: '))
#x = float(input('Введите x: '))

#xd = y(a, b, x)

#print(xd)
