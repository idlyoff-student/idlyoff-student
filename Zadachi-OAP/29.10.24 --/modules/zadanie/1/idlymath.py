import math

def heron_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Стороны не могут образовать треугольник")
    
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
