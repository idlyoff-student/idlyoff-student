total_sum = 0

while True:
    number = int(input("Введите число (100 для завершения): "))
    if number == 100:
        break
    total_sum += number

print("Сумма введенных чисел:", total_sum)
