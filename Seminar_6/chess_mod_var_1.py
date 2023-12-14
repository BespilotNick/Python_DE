# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


ROWS = 8
COLS = 8
START_POINT = 0

def creating_chessboard() -> list:
    return [['_' for _ in range(ROWS)] for _ in range(COLS)]


def not_attacked(board: list, row, col) -> bool:
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def queens_placement(board: list, point: int=START_POINT):
    if point == len(board):
        print_board(board)
        return

    for i in range(len(board)):
        if not_attacked(board, point, i):
            board[point][i] = 'Q'

            queens_placement(board, point + 1)
            board[point][i] = '_'


def print_board(board):
    for row in board:
        print(str(row).replace(',', '\t').replace('\'', ''))
    print()



if __name__ == '__main__':
    queens_placement(creating_chessboard())

