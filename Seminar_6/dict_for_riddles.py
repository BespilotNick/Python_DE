
from riddles_riddles import *

def storage():

    puzzles = {
        'Зимой и летом одним цветом.': ['Ёлка', 'Елка', 'Ёлочка', 'Елочка', 'Ель', 'Пихта'],
        'Сидит дед, во сто шуб одет.': ['Лук', 'Луковица'],
        'Не лает, не кусает, в дом не пускает.': ['Замок', 'Домофон']
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(result)


if __name__ == '__main__':
    storage()