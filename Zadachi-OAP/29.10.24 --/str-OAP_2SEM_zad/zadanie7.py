#src: Определить, сколько раз в тексте встречается заданное слово.

text = input('Введите текст: ')
word_to_count = input("Введите заданное слово: ")
count = 0

text_lower = text.lower()
word_to_count_lower = word_to_count.lower()

# Разбиваем текст на слова
words = text_lower.split()

# Считаем количество вхождений
for word in words:
    if word == word_to_count_lower:
        count += 1

print("Слово '{}' встречается {} раз(а) в тексте.".format(word_to_count, count))
