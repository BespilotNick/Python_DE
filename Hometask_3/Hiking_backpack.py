# Создайте словарь  со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи  влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# * Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 15_000     # грамм, все остальные вещи, то же будем измерять в граммах

things = {
    'Палатка': 8_000,
    'Спальник': 1_000,
    'Спички': 100,
    'Фонарь': 300,
    'Аккумулятор': 500,
    'Телефон': 300,
    'Термос': 500,
    'Котелок': 700,
    'Сковородка': 500,
    'Горелка': 500,
    'Мультитул': 300,
    'Топор': 1_000,
    'Пила': 400,
    'Аптечка': 800,
    'Веревка': 1_000,
    'Карабины': 500,
    'Компас': 200,
    'Миска': 250,
    'Кружка': 150,
    'Еда': 2_500,
    'Вода': 1_500
}

mass = 0
backpack = {}

for key, value in things.items():
    if (mass + value) < MAX_WEIGHT:
        backpack.setdefault(key, value)
        mass += value

print(f'В рюкзак поместилось: {list(backpack.keys())}.\nОбщий вес рюкзака: {mass}')