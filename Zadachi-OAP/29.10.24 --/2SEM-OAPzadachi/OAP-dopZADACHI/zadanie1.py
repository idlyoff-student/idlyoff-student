total_sum = 0
count = 0

number = int(input("Введите число (0 для завершения): "))

while number != 0:
    total_sum += number
    count += 1
    number = int(input("Введите число (0 для завершения): "))  

print("Сумма всех чисел:", total_sum)
print("Количество всех чисел:", count)
