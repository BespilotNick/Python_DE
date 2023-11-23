BIN = 2
OCT = 8

num = int(input('Введите целое число: '))

for div in (BIN, OCT):
    result: str = ''
    test_num: int = num
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div
    print(f'For {div=} {result=}')

print(f' binary = {bin(num)}, oct = {oct(num)}')