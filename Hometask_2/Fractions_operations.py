# Напишите программу, которая принимает две строки вида “a / b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение * дробей.
# Для проверки своего кода используйте модуль  fractions

import fractions
import math

user_fr_1 = input('Введите первую дробь:  ')
user_fr_2 = input('Введите вторую дробь:  ')

lst_1 = user_fr_1.split("/")
lst_2 = user_fr_2.split('/')

numerator_1 = int(lst_1[0])
denominator_1 = int(lst_1[1])
numerator_2 = int(lst_2[0])
denominator_2 = int(lst_2[1])

# Сложение:

if denominator_1 != denominator_2:
    denom_common = denominator_1 * denominator_2
    numer_1 = numerator_1 * denominator_2
    numer_2 = numerator_2 * denominator_1
    sum_frs = str(numer_1 + numer_2) + '/' + str(denom_common)
else:
    sum_frs = str(numerator_1 + numerator_2) + '/' + str(denominator_1)

# Сокращяем дробь:

gcd_sum = math.gcd(int(sum_frs.split('/')[0]), int(sum_frs.split('/')[1]))

if gcd_sum > 1:
    res_numer_sum = int((int(sum_frs.split('/')[0]) / gcd_sum))
    res_denom_sum = int((int(sum_frs.split('/')[1]) / gcd_sum))
    res_sum = str(res_numer_sum) + '/' + str(res_denom_sum)
else:
    res_sum = sum_frs

print(f'Сумма дробей {user_fr_1} и {user_fr_2} равна: {res_sum}')

# Умножение:

mult_frs = str(numerator_1 * numerator_2) + '/' + str(denominator_1 * denominator_2)

# Сокращяем дробь:

gcd_mult = math.gcd(int(mult_frs.split('/')[0]), int(mult_frs.split('/')[1]))

if gcd_mult > 1:
    res_numer_mult = int((int(mult_frs.split('/')[0]) / gcd_mult))
    res_denom_mult = int((int(mult_frs.split('/')[1]) / gcd_mult))
    res_mult = str(res_numer_mult) + '/' + str(res_denom_mult)
else:
    res_mult = mult_frs

print(f'Произведение дробей {user_fr_1} и {user_fr_2} равно: {res_mult}')


# Проверка:
f1 = fractions.Fraction(int(lst_1[0]), int(lst_1[1]))
f2 = fractions.Fraction(int(lst_2[0]), int(lst_2[1]))
print(f'Проверка: сумма {f1} и {f2} = {f1 + f2}')
print(f'Проверка: произведение {f1} и {f2} = {f1 * f2}')
