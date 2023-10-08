# Напишите фуннкцию, которая создает из файла новый с данными в формате JSON.
# Имена (ключи) с большой буквы. Каждая новая пара с новой строки
import csv
import json
import os
import pickle


def create_json(old_file=0, file=0):
    dict_ = dict()
    with open(old_file, 'r', encoding='utf-8') as input_f:
        lines = input_f.readlines()
        for line in lines:
            line = list(line.split(','))
            print(line)
            dict_[line[0].title()] = float(line[1])
    print(dict_)

    with open(file, 'a', encoding='utf-8') as out_f:
        json.dump(dict_, out_f, indent=4, ensure_ascii=False)


# create_json(os.path.join(os.getcwd(), 'dir_for_sem08', 'list_of_corteg.txt'),
#             os.path.join(os.getcwd(), 'dir_for_sem08', 'new_json.json'))

#  Напишите функцию, которая в бесконечном цикле запрашивает имя,
#  личный идентификатор и уровень доступа (от 1 до 7).
#  📌После каждого ввода добавляйте новую информацию в JSON файл.
#  📌Пользователи группируются по уровню доступа.
#  📌Идентификатор пользователя выступает ключём для имени.
#  📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
#  📌При перезапуске функции уже записанные в файл данные должны сохраняться.

def save_in_json(path: str = 'users.json'):
    users_data = {}
    id_list = []
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding="utf-8") as file:
                users_data = json.load(file)
        if users_data:
            for users in users_data.values():
                for user in users:
                    id_list.append(user[1])
        name = input('Name\n')
        if not name:
            break
    while True:
        u_id = input("id\n")
        if u_id.isdigit():
            if int(u_id) not in id_list:
                u_id = int(u_id)
                break
            else:
                print('This ID is already in the database')
        else:
            print('Must be an Integer')
    while True:
        u_lvl = input('lvl\n')
        if u_lvl.isdigit() and 0 < int(u_lvl) < 8:
            break
        else:
            print('Must be between 1 and 7')
    if u_lvl in users_data:
        users_data[u_lvl].append((name, u_id))
    else:
        users_data[u_lvl] = [(name, u_id)]
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(users_data, file, indent=4, ensure_ascii=False)


# save_in_json()

def json_to_csv(json_path, csv_path):
    with open(json_path, 'r', encoding='UTF-8') as json_file, \
            open(csv_path, 'w', encoding='UTF-8') as csv_file:
        data: dict[str, list[str, int]] = json.load(json_file)
        users_list = []
        for u_lvl, users in data.items():
            for user in users:
                users_list.append((user[0], user[1], u_lvl))
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(('Name', 'ID', 'LVL'))
        csv_writer.writerows(users_list)


# json_to_csv('users.json', 'users.csv')


# 📌Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌Дополните id до 10 цифр незначащими нулями.
# 📌В именах первую букву сделайте прописной.
# 📌Добавьте поле хеш на основе имени и идентификатора.
# 📌Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена как отдельный json словарь.
# 📌Имя исходного и конечного файлов передавайте как аргументы функции.

def csv_to_json(csv_path='users.csv', json_path='users.json'):
    with open(csv_path, 'r', encoding='UTF-8') as csv_file, \
            open(json_path, 'w', encoding='UTF-8') as json_file:
        data = csv_file.readlines()
        users_data = {}
        for i in range(len(data)):
            if i and data[i] != '\n':
                user = data[i].strip().replace('"', '').split()
                user[1] = f'{user[1]:0>10}'
                u_hash = str(hash(user[0] + user[1]))
                users_data[u_hash] = user
        json.dump(users_data, json_file, indent=4, ensure_ascii=False)


# csv_to_json()

def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith('.json'):
                file_list.append(os.path.join(files[0], file))
    for file in file_list:
        with open(file.rsplit('.', 1)[0] + '.pickle', 'wb') as data, \
                open(file, 'r', encoding='UTF-8') as json_file:
           users_file = json.load(json_file)
           pickle.dump(users_file, data)

# json_to_pickle()

def pickle_load(path):
    with open(path, 'rb') as data:
        users = pickle.load(data)
        print(users)

pickle_load('users.pickle')