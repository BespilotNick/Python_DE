

from random import randint

def guess(lower: int = 0, upper: int = 100, attempt: int = 10) -> bool:
    r_num = randint(lower, upper)
    for nn in range(1, attempt+1):
        answer = int(input(f'Попытка № {nn}, введите число от {lower} до {upper}:  '))
        if answer > r_num:
            print(f'Ваше число больше загаданного.')
        elif answer < r_num:
            print(f'Ваше число меньше загаданного.')
        else:
            print(f'Вы угадали число. Поздравляем!')
            return  True
    print(f'Попытки закончились. Вы не угадали число.')
    return False
if __name__ == '__main__':
    guess()