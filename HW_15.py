# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='logger.txt', encoding='UTF-8', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def info_of_path(path):
    file_info_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            name, extension = os.path.splitext(file)
            parent_directory = os.path.basename(root)
            file_info = FileInfo(name, extension, False, parent_directory)
            file_info_list.append(file_info)
            logging.info(f'File: {name}, Extension: {extension}, Is Directory: False, Parent Directory: {parent_directory}')
        for directory in dirs:
            parent_directory = os.path.basename(root)
            file_info = FileInfo(directory, '', True, parent_directory)
            file_info_list.append(file_info)
            logging.info(f'Directory: {directory}, Extension: , Is Directory: True, Parent Directory: {parent_directory}')
    return file_info_list

# if __name__ == '__main__':
#     path = input("Введите путь: ")
#     file_info_list = info_of_path(path)
#     print(file_info_list)

# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if b is None else b

    def length(self):
        logging.info(f'Периметр: {(self.a + self.b) * 2}')
        return (self.a + self.b) * 2

    def area(self):
        logging.info(f'Площадь: {self.a * self.b}')
        return self.a * self.b

    def sub(self, other):
        if isinstance(other, Rectangle):
            res = Rectangle.length(self) - Rectangle.length(other)
            if res < 0:
                logging.error("Получается отрицательное число!")
                return "Получается отрицательное число!"
            else:
                return Rectangle(self.a - other.a, self.b - other.b)
        else:
            logging.error("Неверный тип аргумента")
            raise TypeError("Неверный тип аргумента")

    def add(self, other):
        if isinstance(other, Rectangle):
            res = Rectangle.length(self) + Rectangle.length(other)
            if res < 0:
                logging.error("Получается отрицательное число!")
                return "Получается отрицательное число!"
            else:
                logging.info(f'{Rectangle(self.a + other.a, self.b + other.b)}')
                return Rectangle(self.a + other.a, self.b + other.b)
        else:
            raise TypeError("Неверный тип аргумента")

    def eq(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            logging.error("Неверный тип аргумента")
            raise TypeError("Неверный тип аргумента")

    def lt(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            logging.error("Неверный тип аргумента")
            raise TypeError("Неверный тип аргумента")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Операции")
    parser.add_argument("a", type=int, help="Длина")
    parser.add_argument("-b", type=int, help="Ширина")
    args = parser.parse_args()
    rectangle = Rectangle(args.a, args.b)
    logging.info(f'{Rectangle(args.a, args.b)}')
    print("Периметр:", rectangle.length())
    print("Площадь:", rectangle.area())
