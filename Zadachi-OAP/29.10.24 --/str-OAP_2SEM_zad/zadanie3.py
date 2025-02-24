#src: В строке удалить символ точку (.) и подсчитать количество удаленных символов.

text = input("Введите текст: ")
count = 0

new_text = ""
for char in text:
    if char == '.':
        count += 1
    else:
        new_text += char

print("Новый текст:", new_text)
print("Количество удаленных символов:", count)
