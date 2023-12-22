import json
from pathlib import Path


def convert(file: Path) -> None:
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            my_dict[name.title()] = float(number)

    with open(f'{file.stem}.json', 'w', encoding='utf-8') as f_write:
        json.dump(my_dict, f_write, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    convert(Path('results.txt'))
