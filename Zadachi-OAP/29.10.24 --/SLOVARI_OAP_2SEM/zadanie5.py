favorite_songs = {
    'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
    'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
    'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
}
print("Количество любимых песен Димы:", len(favorite_songs['Дима']))  # выведет количество песен Димы
print("Все любимые песни Сони:", ", ".join(favorite_songs['Соня']))  # выведет песни Сони
