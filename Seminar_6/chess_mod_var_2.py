# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 4. Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


# Условие для проверки = (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))

from random import randint

ROWS = 8
COLS = 8

list_coord_1 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
list_coord_2 = [(1, 8), (2, 4), (3, 2), (4, 7), (5, 5), (6, 3), (7, 1), (8, 4)]
list_coord_3 = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]  # Правильный
list_coord_4 = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]  # Правильный


def creating_chessboard() -> list:
    return [[0 for _ in range(ROWS)] for _ in range(COLS)]


def filling_board(board: list, list_coord: list) -> list:
    for pair in list_coord:
        row, col = pair
        board[row - 1][col - 1] = 1
    return board


def checking(list_coord: list) -> bool:
    for i in range(len(list_coord) - 1):
        for j in range(i + 1, len(list_coord)):
            if list_coord[i][0] == list_coord[j][0] \
                    or list_coord[i][1] == list_coord[j][1] \
                    or abs(list_coord[i][0] - list_coord[j][0]) == abs(list_coord[i][1] - list_coord[j][1]):
                return False
    return True


def show_result(list_coord: list):
    if checking(list_coord):
        print(f'Все установленные ферзи "мирные" (пересечений нет)')
    else:
        print(f'В данном варианте имеются "атакующие" ферзи (есть пересечения)')


if __name__ == '__main__':
    show_result(list_coord_1)
    show_result(list_coord_2)
    show_result(list_coord_3)
    show_result(list_coord_4)