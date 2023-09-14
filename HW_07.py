# Задача с семинара:
# ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔Каждая группа включает файлы с несколькими расширениями.
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os


def sorting_file(way):
    ls_dir = os.listdir(way)
    ext_text = ['txt', 'doc']
    ext_jpg = ['jpg', 'jpeg', 'gif']
    ext_video = ['avi', 'mp4']
    for el in ls_dir:
        lst_file = el.split('.')
        if len(lst_file) > 1:
            if lst_file[-1] in ext_text:
                os.mkdir(os.path.join(way, 'text'))
                os.replace(os.path.join(way, el), os.path.join(way, 'text', el))
            if lst_file[-1] in ext_jpg:
                os.mkdir(os.path.join(way, 'images'))
                os.replace(os.path.join(way, el), os.path.join(way, 'images', el))
            if lst_file[-1] in ext_video:
                os.mkdir(os.path.join(way, 'video'))
                os.replace(os.path.join(way, el), os.path.join(way, 'video', el))


# sorting_file('E:\PYTHON\Seminar\dir_with_files')

# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение
def group_rename_files(qty_of_digits, ex_old_file, ex_new_file, range_old_name_file, new_part_name=''):
    lst_files = [i for i in os.listdir('files_for_rename') if i.split('.')[1] == ex_old_file]
    for num, el in enumerate(lst_files,
                             start=1):  # знаю, что выглядит это отвратительно, но работает =( Прошу меня простить
        number = str(0 * (qty_of_digits - len(str(num)))) + str(num)
        os.rename(os.path.join('files_for_rename', el), os.path.join('files_for_rename',
                                                                     f'{new_part_name}_{(el.split(".")[0])[range_old_name_file[0]:range_old_name_file[1] + 1]}_{number}.{ex_new_file}'))


group_rename_files(4, 'txt', 'doc', [0, 2], new_part_name='new_file')

# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
# пакет work_with_files