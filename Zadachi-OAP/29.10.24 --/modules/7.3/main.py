#создайте в отдельном модуле функцию для вычисления выражения: 
from formula import this_fromula

def answer():
    x = float(input('Введите число X: '))
    result = this_fromula(x)
    print(f'Ответ по формуле: {result}' )

if __name__ == "__main__":
    answer()

