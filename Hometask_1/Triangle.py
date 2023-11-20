# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
# предполагаемого треугольника.Требуется сравнить длину каждого отрезка - стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
# существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

A = float(input('Введите длину стороны А: '))
B = float(input('Введите длину стороны B: '))
C = float(input('Введите длину стороны C: '))

if (A + B) > C and (A + C) > B and (B + C) > A:
    if A == B and A == C:
        print(f'Треугольник с указанными параметрами является равносторонним')
    elif A == B and A != C:
        print(f'Треугольник с указанными параметрами является равнобедренным')
    else:
        print(f'Треугольник является разносторонним')
else:
    print(f'Треугольник с указанными параметрами не существует')


# С поставленной задачей код справляется (я проверял), но без проверки ввода (и не в виде функции)