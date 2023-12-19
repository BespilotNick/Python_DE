
__all__ = ['create_file']

from random import randint, choices
from string import ascii_lowercase, digits


def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                count: int = 42) -> None:
    for _ in range(count):
        filename = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))) + '.' + extension
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(filename, 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    create_file('bin', count=2)
