# 📌Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# 📌Например отлавливаем ошибку деления на ноль.
import logging


# logger = logging.getLogger(__name__)
# FORMAT = '{asctime:20}-{levelname:20}-{name}:{msg}'
# logging.basicConfig(format=FORMAT, style='{', filename='logger.log', filemode='w', level=logging.DEBUG)
#
#
# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as exp:
#         logger.error(msg=f'{exp}')


# if __name__ == '__main__':
#     div(0, 0)
#     div(0, 1)
#     div(12, 12)


# 📌На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# 📌Напишите аналогичный декоратор, но внутри используйте модуль logging.

def logg(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        logger = logging.getLogger(__name__)
        FORMAT = '{asctime:20}-{levelname:20}-{name}:{msg}'
        logging.basicConfig(format=FORMAT, style='{', filename='logger.log', filemode='w', encoding='UTF-8',
                            level=logging.DEBUG)
        logger.info(f"{args = }; {kwargs = }, {res = }")
        return res

    return wrap


@logg
def funct(a, b):
    return a + b


# funct(2, 2)
# funct(0, 2)
# funct(-9, 2)


# 📌Доработаем задачу 2.
# 📌Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.
#
# from functools import wraps
# import json
# import os
# import logging
#
# FORMAT = '{asctime} {levelname} {name} {funcName} {msg}'
# logging.basicConfig(format=FORMAT, filename='logfile.log', filemode='a', encoding='utf-8', level=logging.INFO,
# style="{")
# logger = logging.getLogger(__name__)
#
#
# def json_safe(func):
# @wraps(func)
# def wrapper(*args, **kwargs):
# result = func(*args, **kwargs)
# str_args = ', '.join([str(arg) for arg in args]) if args else ' '
# str_kwargs = ', '.join([f'{key}={value}' for key, value in kwargs.items()]) if kwargs else ' '
# re_msg = f'{result} -> {str_args} | {str_kwargs}'
# logger.info(msg=re_msg)
#
# return result
#
# return wrapper
#
#
# @json_safe
# def function_(a, b):
# return a + b
#
#
# function_(337, 499)
# function_(0, 555)
# function_(a=23432, b=5645655)
# function_(4560, b=564555)


# 📌Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# 📌Преобразуйте его в дату в текущем году.
# 📌Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime


def date_in_text(st: str):
    number, weekday, month = st.split()
    number = int(''.join([ch for ch in number if ch.isdigit()]))
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    months = ['янв', 'фев', 'мар', 'апр', 'ма', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    month = int(''.join([str(i + 1) for i in range(len(months)) if month.startswith(months[i])]))
    date = datetime(int(datetime.now().year), month, 1)
    first_month = date.weekday()
    weekdays = weekdays[first_month:] + weekdays[:first_month]

    i = 0
    while number > 0:
        if weekdays[i % 7] == weekday:
            number -= 1
        i += 1
    return i


# print(date_in_text('1-ой понедельник ноября'))

# 📌Дорабатываем задачу 4.
# 📌Добавьте возможность запуска из командной строки.
# 📌При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.
# 📌*Научите функцию распознавать не только текстовое названия
# дня недели и месяца, но и числовые, т.е не мая, а 5.


from datetime import datetime
from sys import argv

WEEKDAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
MONTHS = ['январь', 'февраль', 'март', 'апрель',
          'май', 'июнь', 'июль', 'август',
          'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
CUT_MONTHS = ['янв', 'фев', 'мар', 'апр', 'ма', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


def check_week_day(data: str):


    number, weekday, month = data.split()
    number = int(number[:1])

    month = int(''.join([str(i + 1) for i in range(len(CUT_MONTHS)) if month.startswith(CUT_MONTHS[i])]))
    date = datetime(2023, month, 1)
    first_month = date.weekday()
    weekdays = WEEKDAYS[first_month:] + WEEKDAYS[:first_month]

    i = 0
    while number > 0:
        if weekdays[i % 7] == weekday:
            number -= 1
        i += 1
    return i

if __name__ == '__main__':
    if len(data := argv[1:]) > 0:
        month = MONTHS[datetime.now().month - 1]
        weekday = WEEKDAYS[datetime.now().weekday()]
        number = 1
        for i in range(len(data)):
            if data[i] in WEEKDAYS:
                weekday = data[i]
            for mnt in CUT_MONTHS:
                if data[i].startswith(mnt):
                    month = data[i]
            for ch in data[i]:
                if ch == '-':
                    number = data[i]
        data = ' '.join([f'{number}-ая', weekday, month])
        print(data)
    else:
        data = input('Введите, что будем искать: ')

print(check_week_day(data))
