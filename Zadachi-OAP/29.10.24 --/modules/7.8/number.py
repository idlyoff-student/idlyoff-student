import random

def cubik():
    
    results = []
    
    for i in range(0, 2):
        player = int(input(f'{i+1} игрок! Добро пожаловать в игру. Чтобы бросить кубик, введите 1 (для выхода, напишите 0): '))
        if player == 0:
            break
        elif player == 1:
            result = random.randint(1, 6)
            results.append(result)
            print(f'На вышем игральном кубике выпало число: {result}')
        else:
            print('Введите число 1 или 0.')
    
    if len(results) == 2:
        if results[0] > results[1]:
                print('Поздравляем! Победил игрок 1!')
        elif results[0] < results[1]:
            print('Поздравляем! Победил игрок 2!')
        else:
            print('Ничья.')
    else:
        print('Игра продолжается!')
