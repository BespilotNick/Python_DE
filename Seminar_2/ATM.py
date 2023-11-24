# Игрушечный банкомат

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3


account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Выберите действие:\nПополнить - {CMD_DEPOSIT}, снять - {CMD_WITHDRAW}, Выйти - {CMD_EXIT}    ')
    if command == CMD_EXIT:
        print(f'Заберите Вашу карту, остаток - {account} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан налог на богатство {RICHNESS_TAX * 100} % в размере {percent} у.е.'
              f'Итого на карте осталось {account} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))
    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        print(f'Счет пополнен на {amount} у.е.\nБаланс счёта - {account} у.е.')
    elif command == CMD_WITHDRAW:
        withdraw_tax = amount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if account >= amount + withdraw_tax:
            account -= (amount + withdraw_tax)
            count += 1
            print(f'Вы сняли со счёта {amount} у.е.\nКомиссия за снятие - {withdraw_tax} у.е.\n'
                  f'На счёте осталось {account} у.е.')
        else:
            print(f'Недостаточно денег для выполнения операции:\n'
                  f'Затребованная сумма - {amount} у.е.\nКомиссия составляет - {withdraw_tax} у.е.\n'
                  f'Остаток на счете - {account} у.е.')
    if count and count % COUNT_OPER == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счёт начислено {ADD_PERCENT * 100} % от остатка, что составило -  {bonus_percent} у.е.\n'
              f'Итого на счёте {account} у.е.')