#src: В строке заменить все заглавные буквы строчными.

text = input("Введите текст: ")
new_text = ""

for char in text:
    if char.isupper():
        new_text += char.lower()
    else:
        new_text += char

print("Новый текст:", new_text)
