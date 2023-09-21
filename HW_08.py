# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов
import os


def reqursive_work_with_the_directory(dir_in: str = os.getcwd()):
    res = []
    for topdir, dirs, files in os.walk(dir_in):
        dict_of_dir = {
            "adress": topdir,
            "is_dir": True,
            "size_dir": str(sum(os.path.getsize(os.path.join(topdir, file)) for file in files))
        }
        res.append(dict_of_dir)
        for file in files:
            dict_of_file = {
                "adress": os.path.join(topdir, file),
                "is_dir": False,
                "size_file": str(os.path.getsize(os.path.join(topdir, file)))
            }
            res.append(dict_of_file)
    print(*res, sep='\n')


reqursive_work_with_the_directory('E:\PYTHON\Seminar\work_with_files')
