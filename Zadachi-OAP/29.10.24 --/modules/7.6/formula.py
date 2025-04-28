import math

def formula_answer(x,y):
    formula = (x + (2 + y) / (x ** 2)) / (y + 1 / math.sqrt(x ** 2 + 10))
    return formula

def q_answer(x,y):
    q = 2.8 * math.sin(x + abs(y))
    return q