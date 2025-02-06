# ВАРИАНТ 7
# SRC code

input_string = input("Введите строку: ")
n = len(input_string)
half_n = n // 2
char_list = list(input_string)
i = 0

while True:
    if i >= half_n:
        break
    if char_list[i] == 'п':
        char_list[i] = '*'
    i += 1

result_string = ''.join(char_list)
print("Результат:", result_string)
