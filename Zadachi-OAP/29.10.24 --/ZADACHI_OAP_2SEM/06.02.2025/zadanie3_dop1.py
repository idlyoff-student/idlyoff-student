# ВАРИАНТ 10
# scr code: 2. Дан одномерный массив из 15 элементов. Элементам массива меньше 10 присвоить нулевые значения, а элементам больше 20 присвоить 1. Вывести на экран монитора первоначальный и преобразованный массивы в строчку.

arr = list(map(int, input("Введите 15 целых чисел через пробел: ").split()))

transformed_arr = []
for num in arr:
    if num < 10:
        transformed_arr.append(0)
    elif num > 20:
        transformed_arr.append(1)
    else:
        transformed_arr.append(num)

print("Первоначальный массив:", arr)
print("Преобразованный массив:", transformed_arr)
