# var xddd :)))):D

odd_numbers = []

for i in range(3):
    num = int(input(f"Введите нечетное число {i + 1}: "))
    if num % 2 == 0:
        print("Ошибка: введено четное число. Пожалуйста, перезапустите программу и введите нечетное число.")
        break
    odd_numbers.append(num)

if len(odd_numbers) == 3:    # Вычисление произведения
    product = (odd_numbers[0] ** 2 * odd_numbers[1] ** 2 * odd_numbers[2] ** 2) / 8
    print(f"Произведение шести чисел: {product}")
