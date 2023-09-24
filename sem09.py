# 📌Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

# 📌Дорабатываем задачу 1.
# 📌Превратите внешнюю функцию в декоратор.
# 📌Он должен проверять входят ли переданные в функцию
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌Если не входят, вызывать функцию со случайными числами из диапазонов.
import json
import os
import random


def check_nums(func):
    def wrapper(lo, hi, tri):
        if lo == 1 and hi == 100 and 0 < tri < 11:
            res = func(lo, hi, tri)
        else:
            a, b = random.randint(1, 100), random.randint(1, 100)
            res = func(min(a, b), max(a, b), tri)
        return res

    return wrapper


@check_nums
def guess_number(low=1, high=100, tries=10):
    number = random.randint(low, high)

    def guess_game():
        count = 1
        while count <= tries:
            my_num = int(input(f'Попытка № {count}.\nВведите число\n'))
            if my_num > number:
                print('Я загадал меньше')
            elif my_num < number:
                print('Я загадал больше')
            else:
                print(f'Угадал, число {number}')
                break
            count += 1
        else:
            print(f'Проиграл. Все попытки кончились. Число было {number}')

    return guess_game


game = guess_number(1, 100, 10)


# game()

# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌Имя файла должно совпадать с именем декорируемой функции.

def json_save(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not os.path.isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
                json.dump({str(*kwargs.values()): res}, f, indent=4, ensure_ascii=False)
        else:
            with open(f'{func.__name__}.json', 'r', encoding='UTF-8') as f1:
                json_data = json.load(f1)
            with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f2:
                json_data[str(*kwargs.values())] = res
                json.dump(json_data, f2, indent=4, ensure_ascii=False)
        return res

    return wrapper


@json_save
def function(a, b):
    return a + b


function(5, b=10)
function(10, b=12)
function(10, b=15)
function(10, b=17)


# 📌Создайте декоратор с параметром.
# 📌Параметр - целое число, количество запусков декорируемой функции.

def decorator(loop: int):
    def inner(func):
        res = []

        def wrapper(*args, **kwargs):
            for _ in range(loop):
                res.append(func(*args, **kwargs))
            return res

        return wrapper

    return inner


@decorator(5)
def func_under_decorator(a, b):
    return a + b


print(func_under_decorator(1, 9))



# 📌Объедините функции из прошлых задач.
# 📌Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌Выберите верный порядок декораторов.

# @decorator
# @json_save
# @check_nums
# def random_func():
#   pass


# Сделать шестую задачу
