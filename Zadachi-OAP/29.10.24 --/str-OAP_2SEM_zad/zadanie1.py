#src: Дана строка, содержащая русскоязычный текст. Найти количество слов, начинающихся с буквы "е".

text = input("Введите текст: ")
words = text.split()
count = 0

for word in words:
    if word.lower().startswith('е'):
        count += 1

print("Количество слов, начинающихся с буквы 'е':", count)
