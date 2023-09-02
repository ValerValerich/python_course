# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны

from random import choice

_dict_puzz_and_trise = {}

def puzz(puzzle, answers, tries=5):
    print(puzzle)
    for i in range(1, tries + 1):
        user_answer = input("Введите ответ: ")
        if user_answer in answers:
            print(f"Угадал с попытки № {i}!")
            save_res(puzzle, i)
            break
        else:
            print("Попробуй еще раз")

    else:
        print(f"Попытки кончились!\nБыло загадано {answers[0]}")
        save_res(puzzle, 'Не угадано!')


# puzz("Зимой и летом одним цветом?", ['ель', 'елка', 'ёлочка'], 5)


# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки

def random_puzz():
    puzzles_dict = {'Висит груша, нельзя скушать?': ['лампочка', 'лампа'],
                    'Зимой и летом одним цветом?': ['ель', 'елка', 'ёлка'],
                    'Не лает, не кусает, в дом не пускает?': ['замок', 'замочек', 'кодовый замок']}
    while puzzles_dict:
        rnd_puzz = choice(list(puzzles_dict.keys()))
        valve = puzzles_dict.pop(rnd_puzz)
        puzz(rnd_puzz, valve)
    print('Вы великолепны!')


def save_res(puzz, trise):
    _dict_puzz_and_trise[puzz] = trise

def show_res(dct: dict):
    print(*(f'Загадка:\n{k}\nОтгадана с попытки № {v}' for k, v in dct.items()), end='\n')

random_puzz()
show_res(_dict_puzz_and_trise)