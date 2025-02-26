#src: В строке удалить все буквы "а"  и подсчитать количество удаленных символов.

input_string = input('Введите текст: ')
count = 0
new_string = ""

for char in input_string:
    if char != 'а':
        new_string += char
    else:
        count += 1

print("Новая строка:", new_string)
print("Количество удаленных 'а':", count)
