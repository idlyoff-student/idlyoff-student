import formula

def go():
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))
    
    main_formula = formula.formula_answer(x,y)
    q = formula.q_answer(x,y)
    
    print(f'Ответ главного выражения: {main_formula}')
    print(f'Ответ Q: {q}')



if __name__ == '__main__':
    go()