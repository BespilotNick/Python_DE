# Напишите функцию для транспонирования матрицы

from random import randint

def creating_matrix():
    rows = int(input(f'Выберите количество строк в матрице: '))
    cols = int(input(f'Выберите количество столбцов в матрице: '))

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    command = int(input('Если желаете заполнить матрицу самостоятельно, введите 1; для автозаполнения выберите опцию:  '
                        'симметричная матрица - 2, случайное заполнение  - 3   '))

    if command == 1:
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = input(f'Введите значение элемента: ')
    elif command == 2:
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = i + j
    else:
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = randint(0, sum(len(row) for row in matrix))

    print(f'Исходная матрица: ')
    for row in matrix:
        print(f'{row}')
    print()

    return matrix

def transposing_matrix(matrix: list) -> list:
    t_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t_matrix[j][i] = matrix[i][j]

    print(f'Транспонированная матрица: ')
    for row in t_matrix:
        print(f'{row}')

    return t_matrix

transposing_matrix(creating_matrix())