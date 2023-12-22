from typing import TextIO
from pathlib import Path


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert_lines(names: str | Path, numbers: str | Path, results: str | Path) -> None:
    with (
        open('names.txt', 'r', encoding='utf-8') as f_names,
        open('numbers.txt', 'r', encoding='utf-8') as f_numbers,
        open('results.txt', 'a', encoding='utf-8') as f_results
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_names, len_numbers)

        for _ in range(max_len):
            name = read_line_or_begin(f_names)
            nums_str = read_line_or_begin(f_numbers)
            num_i, num_f = map(float, nums_str.split('|'))
            multip = num_i * num_f
            if multip < 0:
                f_results.write(f'{name.lower()} {-multip}\n')
            elif multip > 0:
                f_results.write(f'{name.upper()} {int(multip)}\n')


if __name__ == '__main__':
    convert_lines(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))
