# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

import typing

def rev_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, typing.Hashable):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict

print(rev_dict(bananas = 23, apples = (5, 12), oranges = [12, 24], pineapples = 'five'))