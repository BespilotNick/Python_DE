from random import randint, uniform
from pathlib import  Path

MIN_NUMBER = -1_000
MAX_NUMBER = 1_000


def fill_num(filename: str| Path, count: int) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUMBER, MAX_NUMBER)
            num_float = uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{num_int}|{num_float}\n')


if __name__ == '__main__':
    fill_num(Path('numbers.txt'), count=256)