# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
#       Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
#       исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
#       Далее счётчик файлов и расширение.


__all__ = ['group_renaming']

from Seminar_7.task_6 import generate_file, create_file
import os
from pathlib import Path


def group_renaming(new_name: str = 'new_name', len_nn: int = 3, start_extension: str = 'bin',
                   final_extension: str = 'txt', range_orig_name: tuple = (0, 5)) -> None:
    nn = 1
    print(os.listdir())
    for obj in os.listdir():
        if os.path.isfile(obj):
            file_name, extension = obj.split('.')
            if extension == start_extension:
                final_name = ''.join((file_name[range_orig_name[0]:range_orig_name[1]]) + new_name +
                                     str(nn).zfill(len_nn) + '.' + final_extension)
                nn += 1
                os.rename(obj, final_name)
        elif os.path.isdir(obj):
            os.chdir(Path(obj))
            group_renaming()
            os.chdir('..')


if __name__ == '__main__':
    # create_file(extension='bin', count=4)         # Это для проверки, вроде работает.
    # generate_file('new_dir', txt=3)
    # generate_file('new_dir', bin=3)
    # generate_file('new_dir', jpg=3)
    group_renaming()
