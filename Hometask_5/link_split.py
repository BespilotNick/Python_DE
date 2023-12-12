# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

my_path = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'

# abs_path = input(f'Укажите абсолютный путь до файла:  ')

def path_to_tuple(path):

    *f_path, ext_name = path.split('.')
    file_path = ''.join(f_path)
    extension, file_name = ext_name.split('#')

    result = file_path, file_name, extension

    return result

print(f'Путь = {path_to_tuple(my_path)[0]}\nИмя файла = {path_to_tuple(my_path)[1]}\nРасширение файла = {path_to_tuple(my_path)[2]}' )
print(f'{path_to_tuple(my_path)=}')