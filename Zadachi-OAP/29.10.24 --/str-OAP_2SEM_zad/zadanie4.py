#src: В строке заменить букву(а) буквой (о). Подсчитать количество замен. Подсчитать, сколько символов в строке.

text = input("Введите текст: ")
count = 0
new_text = ""

for char in text:
    if char == 'а':
        new_text += 'о'
        count += 1
    else:
        new_text += char

length = len(text)

print("Новый текст:", new_text)
print("Количество замен:", count)
print("Количество символов в строке:", length)
