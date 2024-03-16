"""
 Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
  В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""
film = {'title': 'Турецкий гамбит',
        'director': 'Джаник Файзиев',
        'year': '2005',
        'budget': '$4 000 000',
        'main_actor': 'Эраст Фандорин',
        'slogan': 'Титулярный советник Эраст Фандорин участвует в русско-турецкой войне.'}
for key in film.keys():
    print(f"{key}")
for value in film.values():
    print(f"{value}")
for key, value in film.items():
    print(f"{key}: {value}")
