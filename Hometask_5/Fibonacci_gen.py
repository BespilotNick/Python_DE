# Создайте функцию генератор чисел Фибоначчи

user_num = int(input('Введите желаемое количесто значений ряда Фибоначчи: '))

def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f'Последовательность Фибоначчи из {user_num} элементов: {list(fibonacci_gen(user_num))}')
