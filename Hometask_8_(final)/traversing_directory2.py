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
    res_dict = {}

    obj_list = []
    path_list = []
    parent_list = []
    type_list = []
    size_list = []

    for path, *objects in os.walk(top=directory):
        for sub_list in objects:
            if isinstance(sub_list, list):
                obj_list.extend(sub_list)
            for elem in sub_list:
                path_list.append(os.path.join(path, elem))
                parent_list.append(path)

                if os.path.isfile(os.path.join(path, elem)):
                    type_list.append('File')
                elif os.path.isdir(os.path.join(path, elem)):
                    type_list.append('Directory')
                else:
                    type_list.append('Not a File and Not a Directory')




    print(obj_list)
    print()
    # print(path_list)
    # print()
    # print(parent_list)
    print()
    print(type_list)
    # size_list = list(os.path.getsize(i) for i in path_list if os.path.isfile(i)
    #         else sum(os.path.getsize(os.path.join(path, name)) for name in file_name))
    # print(size_list)

    #     #     print(os.path.getsize(os.path.join(dir_path, file_name)))
    #
    # print(res_dict)

    # with open('traversed_directory2.json', 'w', encoding='utf-8') as fjson_write:
    #     json.dump(res_dict, fjson_write, indent=2, ensure_ascii=False)
    #
    # with open('traversed_directory2.pickle', 'wb') as fpick_write:
    #     pickle.dump(res_dict, fpick_write)
    #
    # list_rows = []
    # with open('traversing_directory2.csv', 'w', newline='', encoding='utf-8') as fcsv_write:
    #     csv_write = csv.DictWriter(fcsv_write,
    #                                fieldnames=['Main Directory', 'Parent Directory', 'Object_name', 'Type', 'Size'],
    #                                dialect='excel-tab')
    #     csv_write.writeheader()
    #     csv_write.writerow(list_rows)




if __name__ == '__main__':
    traversing_directory(Path('D:\\GeekBrains\\DATA ENGINEER\\Python DE\\Hometask_8_(final)\\Copy_S_7_for_test'))
