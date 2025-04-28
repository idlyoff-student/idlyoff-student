import random

def play_game():

    secret_num = random.randint(1, 10)
    user_answer = int(input("Введи случайное число от 1 до 10: "))

    if secret_num == user_answer:
        print('Ты выиграл!')
    else:
        print('Неудача! Повтори попытку еще раз.')