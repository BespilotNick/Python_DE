# Возьмите задачу о  банкомате  из семинара 2.  Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


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

global account
global count
global amount
global operations_log

account = decimal.Decimal(0)
count = 0
operations_log = {
    'Пополнения': [],
    'Снятия': []
}

def interface():
    global account
    global count
    global amount

    while True:
        command = input(f'Выберите действие:\nПополнить - {CMD_DEPOSIT}, снять - {CMD_WITHDRAW}, Выйти - {CMD_EXIT}   ')
        if command == CMD_EXIT:
            finish_programm()
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
            deposit(amount)
        elif command == CMD_WITHDRAW:
            withdraw(amount)
        if count and count % COUNT_OPER == 0:
            bonus()


def deposit(sum):
    global account
    global count
    global operations_log

    account += sum
    count += 1
    print(f'Счет пополнен на {sum} у.е.\nБаланс счёта - {account} у.е.')
    operations_log['Пополнения'].append(sum)


def withdraw(sum):
    global account
    global count
    global operations_log

    withdraw_tax = sum * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                    MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    if account >= sum + withdraw_tax:
        account -= (sum + withdraw_tax)
        count += 1
        print(f'Вы сняли со счёта {sum} у.е.\nКомиссия за снятие - {withdraw_tax} у.е.\n'
              f'На счёте осталось {account} у.е.')
    else:
        print(f'Недостаточно денег для выполнения операции:\n'
              f'Затребованная сумма - {sum} у.е.\nКомиссия составляет - {withdraw_tax} у.е.\n'
              f'Остаток на счете - {account} у.е.')
    operations_log['Снятия'].append(sum)


def finish_programm():
    global account
    global operations_log

    print(f'Заберите Вашу карту, остаток - {account} у.е.')
    print(operations_log)
    exit()


def bonus():
    global account
    global amount

    bonus_percent = account * ADD_PERCENT
    account += bonus_percent
    print(f'На счёт начислено {ADD_PERCENT * 100} % от остатка, что составило -  {bonus_percent} у.е.\n'
          f'Итого на счёте {account} у.е.')


interface()
