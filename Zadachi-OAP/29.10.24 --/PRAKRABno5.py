a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a == 0 or b == 0 or c == 0:
    print("Расчет невозможен")
else:
    average = (a + b + c) / 3
    print(f"Среднее арифметическое: {average:.2f}")
