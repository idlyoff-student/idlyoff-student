import math

try:
    x = float(input('Введите значение X: '))
    y = float(input('Введите значение Y: '))
    
    under_sqrt = x**7 - y**3
    
    if under_sqrt < 0:
        print("Ошибка: попытка вычислить квадратный корень из отрицательного числа.")
    else:

        denominator = 3.14 * 3.57 * math.sin(y) + math.sqrt(under_sqrt)
        
        if denominator == 0:
            print("Ошибка: деление на ноль невозможно.")
        else:
           
            f = (x**5 + (math.cos(x**2)**3)) / denominator
            print('Значение f равно:', f)

except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите числовые значения.")
