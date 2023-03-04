def geo(data):
    russian_cities = []
    for visit in data:
      for city, country in visit.values():
        if 'Россия' in country:
          russian_cities.append(visit)
    return russian_cities

# geo_logs = [
#         {'visit1': ['Москва', 'Россия']},
#         {'visit2': ['Дели', 'Индия']},
#         {'visit3': ['Владимир', 'Россия']},
#         {'visit4': ['Лиссабон', 'Португалия']},
#         {'visit5': ['Париж', 'Франция']},
#         {'visit6': ['Лиссабон', 'Португалия']},
#         {'visit7': ['Тула', 'Россия']},
#         {'visit8': ['Тула', 'Россия']},
#         {'visit9': ['Курск', 'Россия']},
#         {'visit10': ['Архангельск', 'Россия']}
#     ]
# print(geo(geo_logs))

def id(data):
    list1 = data.values()
    new_list = []
    for elements in list1:
      for element in elements:
        new_list.append(element)
    new_set = set(new_list)
    return list(new_set)

# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
# print(id(ids))


def pr(data):
    values = data.values()
    max_stat = max(values)
    best_company = (list(data.keys())[list(data.values()).index(max_stat)])
    return f'Канал с максимальным объемом продаж: {best_company}'

# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# print(pr(stats))