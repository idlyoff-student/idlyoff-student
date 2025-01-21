total_sum = 0
count = 0

number = int(input("Введите отрицательное число (положительное для завершения): "))

while number < 0:
    total_sum += number
    count += 1
    number = int(input("Введите отрицательное число (положительное для завершения): "))

if count > 0:
    average = total_sum / count
    print("Среднее арифметическое всех отрицательных чисел:", average)
else:
    print("Не было введено отрицательных чисел.")
