import os
from pathlib import Path
import json
import csv
import pickle

def traversing_directory(directory: str | Path) -> None:

    res_dict = {}
    for dir_path, dir_file, file_name in os.walk(directory):
        res_dict[f'DIRECTORY - {dir_path}'] = [
            f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    with open('traversed_directory.json', 'w', encoding='utf-8') as fjson_write:
        json.dump(res_dict, fjson_write, indent=2, ensure_ascii=False, separators=(',', ':'))

    with open('traversed_directory.pickle', 'wb') as fpick_write:
        pickle.dump(res_dict, fpick_write)

    data = [["Dir", "Files"]]
    for key, value in res_dict.items():
        data.append([key, value])
    with open('traversed_directory.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)



traversing_directory('D:\\GeekBrains\\DATA ENGINEER\\Python DE\\Hometask_8_(final)\\Copy_S_7_for_test')
