def f(x, a):
    if x >= 0:
        return 4 * x + 5 * a**2
    else:
        return 4 * x**2 - 5 * a
    
x1 = float(input('Введите значение для x1: ')) 
a1 = float(input('Введите значение для x1: '))

x2 = float(input('Введите значение для x2: '))  
a2 = float(input('Введите значение для а2: ')) 

result1 = f(x1, a1)
result2 = f(x2, a2)

print(f"f({x1}, {a1}) = {result1}")
print(f"f({x2}, {a2}) = {result2}")


# РЕШЕНИЕ ЧЕРЕЗ LAMBDA:

#f = lambda x, a: 4 * x + 5 * a**2 if x >= 0 else 4 * x**2 - 5 * a

#x1 = 2  
#a1 = 3  

#x2 = -1  
#a2 = 3  

#result1 = f(x1, a1)
#result2 = f(x2, a2)

#print(f"f({x1}, {a1}) = {result1}")
#print(f"f({x2}, {a2}) = {result2}")
