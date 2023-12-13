
def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count+1):
        answer = input(f'Ваш ответ:  ').capitalize()
        if answer in answers:
            print(f'Правильно! Конечно же это {answer}!')
            print(f'Вы угадали с {nn}й попытки.')
            return nn
        else:
            print(f'Неверно.')
    print(f'Попытки закончились, Вы не угадали.')
    return 0

riddle_text = 'Зимой и летом одним цветом.'
answers = ['Ёлка', 'Елка', 'Ёлочка', 'Елочка', 'Ель', 'Пихта']


def storage():

    puzzles = {
        'Зимой и летом одним цветом.': ['Ёлка', 'Елка', 'Ёлочка', 'Елочка', 'Ель', 'Пихта'],
        'Сидит дед, во сто шуб одет.': ['Лук', 'Луковица'],
        'Не лает, не кусает, в дом не пускает.': ['Замок', 'Домофон']
    }
    for puzzle, answers in puzzles.items():
        result = riddle(puzzle, answers)
        print(result)
        save_result(puzzle, result)

_data = {}

def save_result(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn


def show_results():
    res = (f'Загадку "{puzzle}" отгадали с {nn}й попытки' if nn > 0
           else f'Загадку "{puzzle}" не отгадали'
           for puzzle, nn in _data.items())
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    show_results()