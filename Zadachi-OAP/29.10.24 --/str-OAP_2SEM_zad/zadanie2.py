#scr: В строке заменить все двоеточия (:) знаком процента (%). Подсчитать количество замен.

text = input("Введите текст: ")
count = 0

new_text = ""
for char in text:
    if char == ':':
        new_text += '%'
        count += 1
    else:
        new_text += char

print("Новый текст:", new_text)
print("Количество замен:", count)
