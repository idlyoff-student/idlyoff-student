import math

def calculate_y(a, b, x):

    denominator = 3 * a - abs(x)
    y = (math.cos(b) - math.sqrt(a)) / denominator

    return y

a = float(input('Введите значение A: '))
b = float(input('Введите значение B: '))
x = float(input('Введите значение X: '))

result = calculate_y(a, b, x)
print(f"Значение y: {result}")

#РЕШЕНИЕ ЧЕРЕЗ LAMBDA

#import math

#calculate_y = lambda a, b, x: (math.cos(b) - math.sqrt(a)) / (3 * a - abs(x))

#a = 4  
#b = math.pi / 3 
#x = 2 

#result = calculate_y(a, b, x)
#print(f"Значение y: {result}")
