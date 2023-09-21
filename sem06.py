# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from sys import argv
from random import randint as ri


def guess(start, stop, tries):
    rnd_num = ri(start, stop)
    while tries > 0:
        user_num = int(input("Введите число: "))
        if user_num == rnd_num:
            print("Угадал!")
            break
        elif user_num > rnd_num:
            print("Меньше!")
        else:
            print("Больше!")
        tries -= 1
    else:
        print(f"Попытки кончились!\nБыло загадано {rnd_num}")


# guess(1, 101, 10)


# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

argv = list(map(int, argv[1:]))
# guess(*argv)

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны

# дальше задачки в файле puzzle.py

# • Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# • Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# • Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# • Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# • Проверку года на високосность вынести в отдельную защищённую функцию
# Через стандартный модуль с датами. Пропустил

