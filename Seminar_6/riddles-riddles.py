
def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(count):
        answer = input(f'Ваш ответ:  ').capitalize()
        if answer in answers:
            print(f'ПРАВИЛЬНО, конечно же это {answer}!')
            print(f'Вы угадали с {nn+1}й попытки.')
            return nn
        else:
            print(f'Неверно.')
    print(f'Попытки закончились, Вы не угадали.')
    return 0

riddle_text = 'Зимой и летом одним цветом.'
answers = ['Ёлка', 'Елка', 'Ёлочка', 'Елочка', 'Ель', 'Пихта']

if __name__ == '__main__':
    riddle(riddle_text, answers)
