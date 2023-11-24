# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


# Способ 1: без использования функции hex()! Но с использованием форматирования :)

# while True:
#     user_num = input('Введите число в десятичной системе исчесления:  ')
#     print(format(int(user_num), "x") if user_num.isdigit() else 'Введено некорректное значение')
#
# print(hex(int(user_num)))


# Способ 2: Нормальный (тот который требовался).
#
user_num = ''
result = ''
HEX = 16

while not user_num.isdigit():
    user_num = input('Введите десятичное число для преобразования:  ')

temp_num = int(user_num)
while temp_num > 0:
    if (temp_num % HEX) in range(0, 10):
        result = str(temp_num % HEX) + result
    else:
        if (temp_num % HEX) == 10:
            result = 'a' + result
        elif (temp_num % HEX) == 11:
            result = 'b' + result
        elif (temp_num % HEX) == 12:
            result = 'c' + result
        elif (temp_num % HEX) == 13:
            result = 'd' + result
        elif (temp_num % HEX) == 14:
            result = 'e' + result
        elif (temp_num % HEX) == 15:
            result = 'f' + result
    temp_num //= HEX
print(f'Результат преобразования числа {user_num} в шестнадцатиричную систему = 0x{result}')

print(f'Результат выполнения функции hex() - {hex(int(user_num))}')