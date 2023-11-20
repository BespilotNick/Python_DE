# Сделать таблицу умножения как в школьной тетради (СССР)

LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1

for main_num in (LOWER_LIMIT, LOWER_LIMIT+COLUMN):
    for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
        for f_num in range(main_num, main_num + COLUMN):
            print(f'{f_num:>2} X {s_num:>2} = {f_num * s_num:>2}', end='\t')
        print()
    print()