# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

start_list = [1, 2, 14, 3, 2, 23, 5, 4, 32, 7, 5, 41, 6, 3, 50, 2, 1, 23, 7, 8, 4, 14, 9, 2, 5, 7, 3, 9]
test_set = set()

for i in start_list:
    if start_list.count(i) > 1:
        test_set.add(i)
print(f'В изначальном списке повторяются элемены: {list(test_set)}')