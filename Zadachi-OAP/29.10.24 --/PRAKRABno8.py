# var 3 \\ 25 aud

user_input = input("Введите числа, разделенные пробелами: ")
numbers = user_input.split()
positive_sum = 0
negative_sum = 0

for number in numbers:
    num = int(number)
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num

difference = positive_sum - negative_sum
print("Разность между суммой положительных и отрицательных чисел:", difference)
