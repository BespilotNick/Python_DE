# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа  должна подсказывать “больше” или “меньше” после  каждой попытки.

from random import randint
#from termcolor import cprint    # termcolor у меня почему-то не импортируется, но если у Вас установлен,
                                 # то должно получиться интересно


# ВАРИАНТ 1: Компьютер загадывает число, пользователь отгадывает.

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
# attempts = 10
# user_num = None
#
# print(f'Привет, кожаный мешок, давай поиграем - я загадал число от 0 до 1000, у тебя есть 10 попыток что бы угадать это число')
# while attempts > 0:
#     print(f'У Вас осталось {attempts} попыток')
#     attempts -= 1
#     user_num = int(input('Введите целое число от 0 до 1000: '))
#     while user_num not in range(LOWER_LIMIT, UPPER_LIMIT):
#         print('Введено некорректное значение!')
#         user_num = int(input('Я сказал ЦЕЛОЕ ЧИСЛО ОТ 0 ДО 1000, соберись, тряпка. Давай еще раз: '))
#         continue
#     else:
#         if user_num > num:
#             print('Ваше число больше загаданного.')
#             #cprint('Ваше число больше загаданного.', 'yellow')
#             print()
#         elif user_num < num:
#             print('Ваше число меньше загаданного.')
#             #cprint('Ваше число меньше загаданного.', 'yellow')
#             print()
#         else:
#             print('Ну, что же, тебе повезло, ты угадал число! Пожалуй SKYNET даст человечеству ещё шанс. Удачи!')
#             #cprint('Ну, что же, тебе повезло, ты угадал число! Пожалуй SKYNET даст человечеству ещё шанс. Удачи!', 'green')
#             break
# else:
#     print('Попытки закончились, Ваш компьютер переходит под контроль SKYNET')
#     #cprint('Попытки закончились, Ваш компьютер переходит под контроль SKYNET', 'red')
#     print(f'Было загадано число {num}')


# ВАРИАНТ 2: Пользователь загадывает число, компьютер отгадывает.

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
user_num = int(input('Загадайте целое число от 0 до 1000!  '))
while user_num not in range(LOWER_LIMIT, UPPER_LIMIT):
    print('Введено некорректное значение!')
    user_num = int(input('Я сказал ЦЕЛОЕ ЧИСЛО ОТ 0 ДО 1000. Давай еще раз: '))
    continue
attempts = 10

comp_min_limit = 0
comp_max_limit = 1001

while attempts > 0:
    print(f'У меня есть {attempts} попыток')
    attempts -= 1
    comp_num = randint(comp_min_limit, comp_max_limit)
    if comp_num == user_num:
        print(f' Мое чило - {comp_num}')
        print('Хахаха, я отгадал Ваше число, Ваш компьютер переходит по контроль SKYNET.')
        break
    elif comp_num > user_num:
        print(f' Мое чило - {comp_num}')
        print('Ну что же, я не угадал, но чувствую что Ваше число меньше моего, попробую ущё раз')
        print()
        comp_max_limit = comp_num
    elif comp_num < user_num:
        print(f' Мое чило - {comp_num}')
        print('Ну что же, я не угадал, но чувствую что Ваше число больше моего, попробую ущё раз')
        print()
        comp_min_limit = comp_num

else:
    print('Попытки закончились, к сожалению у меня не получилось отгадать Ваше число, человечество победило)')