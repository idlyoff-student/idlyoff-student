even_count = 0
number = None

while number != 0:
    number = int(input("Введите число (0 для завершения): "))
    
    if number == 0:
        break
    
    if number > 0:
        number = number / 2
    elif number < 0:
        number = number * 2
    
    if number % 2 == 0:
        even_count += 1

print("Количество четных чисел:", even_count)

