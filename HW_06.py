import random

from dateutil.parser import parse  # Попалась удобная библиотека, может еще где сгодится
from sys import argv


# • В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
def check_date(input_text):
    try:
        parse(input_text, fuzzy=True)
        return True
    except ValueError:
        return False


#  argv = argv[1]

#  print(check_date(argv))

# • Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
def chess(*coordinates):
    pull = [[0 for _ in range(8)] for _ in range(8)]
    for x, y in coordinates:
        pull[x - 1][y - 1] = 8
    # print(*pull, sep="\n")

    for i in range(8):
        for j in range(8):
            if i - j == coordinates[i][0] - coordinates[i][1] and i + j == coordinates[i][0] + coordinates[i][1]:
                return False

    if not len(set(coordinates)) == len(coordinates):
        return False
    elif not len(set([i[0] for i in coordinates])) == len(set([i[1] for i in coordinates])) == 8:
        return False
    else:
        return True


# print(chess((1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)))
# print(chess((1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 3)))

# • Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

def random_positions_chess():
    arg_for_chess = set()
    coll = []
    while len(coll) < 4:
        while not len(arg_for_chess) == 8:
            arg_for_chess.add((random.randint(0, 8), random.randint(0, 8)))

        if chess(*arg_for_chess):
            print(*arg_for_chess)
            coll.append(arg_for_chess)
        arg_for_chess.clear()


random_positions_chess()
