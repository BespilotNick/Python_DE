
__all__ = ['generate_file']


from task_4 import create_file


def generate_file(**kwargs) -> None:
    for extension, amount in kwargs.items():
        create_file(extension, count=amount)


if __name__ == '__main__':
    generate_file(bin=2, jpg=1, txt=3)
