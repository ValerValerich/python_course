import os


def group_rename_files(qty_of_digits, ex_old_file, ex_new_file, range_old_name_file, new_part_name=''):
    lst_files = [i for i in os.listdir('files_for_rename') if i.split('.')[1] == ex_old_file]
    for num, el in enumerate(lst_files,
                             start=1):  # знаю, что выглядит это отвратительно, но работает =( Прошу меня простить
        number = str(0 * (qty_of_digits - len(str(num)))) + str(num)
        os.rename(os.path.join('files_for_rename', el), os.path.join('files_for_rename',
                                                                     f'{new_part_name}_{(el.split(".")[0])[range_old_name_file[0]:range_old_name_file[1] + 1]}_{number}.{ex_new_file}'))
