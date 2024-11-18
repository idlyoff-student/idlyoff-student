# var 3 \\ 25 aud

user_input = input("Введите числа, разделенные пробелами: ")

numbers = user_input.split()

for number in numbers:
    num = int(number)
    difference = 100 - num
    print("Разность между 100 и", num, "равна", difference)
