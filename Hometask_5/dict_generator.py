# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Николай', 'Алиса', 'Катерина', 'Вероника', 'Валерия', 'Ирина', 'Жанна']
salaries = [15_000, 13_000, 7_000, 9_000, 12_000, 10_000, 6_000]
rewards = ['180.00%', '120.00%', '85.00%', '110.00%', '125.00%', '97.00%', '10.25%']

sum_rewards = {name: salary * (float(reward.strip('%')) / 100) for name, salary, reward in zip(names, salaries, rewards)}

print(f'Суммы премии в евро: {sum_rewards}')