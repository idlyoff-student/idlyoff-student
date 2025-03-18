friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
friends = {}

for i in range(len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]  # добавляем пары в словарь

print(f"Лена живёт в городе {friends['Лена']}")  # выведет город Лены
