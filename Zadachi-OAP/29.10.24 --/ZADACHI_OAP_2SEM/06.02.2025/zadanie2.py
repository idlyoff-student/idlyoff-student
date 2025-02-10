# ВАРИАНТ 7
# src code: 1. Дан массив целых чисел. Найти сумму элементов с четными номерами и произведение элементов с нечетными номерами. Вывести сумму и произведение.

# Вводим массив целых чисел
input_array = input("Введите целые числа через пробел: ")
numbers = list(map(int, input_array.split()))

# Инициализируем сумму и произведение (еще один метод?)
sum_even_indices = 0
product_odd_indices = 1

# Проходим по элементам массива
for index in range(len(numbers)):
    if index % 2 == 0:  # Четные индексы
        sum_even_indices += numbers[index]
    else:  # Нечетные индексы
        product_odd_indices *= numbers[index]

# Выводим результат
print("Сумма элементов с четными номерами:", sum_even_indices)
print("Произведение элементов с нечетными номерами:", product_odd_indices)
