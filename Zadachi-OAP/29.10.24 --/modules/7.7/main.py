from calcc import calculate_function

def go():
    x = float(input('Введите значение X: '))
    result = calculate_function(x)
    print(f'Ответ: {result}')


if __name__ == '__main__':
    go()