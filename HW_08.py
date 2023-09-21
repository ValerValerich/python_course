# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов
import csv
import json
import os
import pickle


def list_to_json(lst: list):
    temp = {f"{i}": el for i, el in enumerate(lst, 1)}
    with open('list_to.json', 'a', encoding='utf-8') as f:
        json.dump(temp, f, indent=4, ensure_ascii=False)


def list_to_csv(lst: list):
    with open('list_to.csv', 'w', encoding='UTF-8') as f:
        temp = [(a, b, c) for i in lst for a, b, c in [i.values()]]
        csv_writer = csv.writer(f, dialect='excel', delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(('Address', 'is_dir', 'size'))
        csv_writer.writerows(temp)


def list_to_pikle(lst: list):
    with open('list_to.pickle', 'wb') as f:
        pickle.dump(lst, f, protocol=0)


def reqursive_work_with_the_directory(dir_in: str = os.getcwd()):
    res = []
    for topdir, dirs, files in os.walk(dir_in):
        size = 0
        for f in files:
            fp = os.path.join(dir_in, f)
            size += os.path.getsize(fp)
        dict_of_dir = {
            "address": topdir,
            "is_dir": True,
            "size": str(size)
        }
        res.append(dict_of_dir)
        for file in files:
            dict_of_file = {
                "address": os.path.join(topdir, file),
                "is_dir": False,
                "size": str(os.path.getsize(os.path.join(topdir, file)))
            }
            res.append(dict_of_file)
    print(*res, sep='\n')
    list_to_json(res)
    list_to_csv(res)
    list_to_pikle(res)


reqursive_work_with_the_directory('E:\PYTHON\Seminar\work_with_files')
