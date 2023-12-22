# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех
#   вложенных файлов и директорий.


import os
from pathlib import Path
import json
import csv
import pickle


def traversing_directory(directory: Path) -> None:
    os.chdir(directory)
    res_dict = {}
    res_dict[{os.getcwd()}] = {}
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        print(dir_path, dir_name, file_name)
        for i in dir_name:
            print(os.path.getsize(Path(i)))
            # for j in file_name:
            #     print(os.path.getsize(Path(j)))

    # print(res_dict)

    # with open('traversed_directory.json', 'w', encoding='utf-8') as fjson_write:
    #     json.dump(res_dict, fjson_write, indent=2, ensure_ascii=False)
    #
    # with open('traversed_directory.pickle', 'wb') as fpick_write:
    #     pickle.dump(res_dict, fpick_write)
    #
    # list_rows = []
    # with open('traversing_directory.csv', 'w', newline='', encoding='utf-8') as fcsv_write:
    #     csv_write = csv.DictWriter(fcsv_write,
    #                                fieldnames=['Main Directory', 'Parent Directory', 'Object_name', 'Type', 'Size'],
    #                                dialect='excel-tab')
    #     csv_write.writeheader()
    #     csv_write.writerow(list_rows)




if __name__ == '__main__':
    traversing_directory(Path('D:\\GeekBrains\\DATA ENGINEER\\Python DE\\Seminar_7'))
