# var 5 \\ 25 aud
user_input = input("Введите числа, разделенные пробелами: ")

numbers = user_input.split()

total_sum = 0

for number in numbers:
    num = int(number)
    if abs(num) > 10:
        total_sum += num

print("Сумма чисел, по модулю больших 10:", total_sum)
