# 📌Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# 📌Обрабатывайте не числовые данные как исключения.

def input_number():
    while True:
        number = input('Введите целое или вещественное число: ')
        try:
            return int(number)
        except:
            try:
                return float(number)
            except:
                print('Это не число. Попробуйте еще раз')


# print(input_number())

# 📌Создайте функцию аналог get для словаря.
# 📌Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌Реализуйте работу через обработку исключений.


dict_1 = {1: 'one', 2: 'two'}


def our_get(dct: dict, key, default_value=None):
    try:
        return dct[key]
    except KeyError:
        return default_value
    except TypeError:
        return 'Ошибка типа ключа'


# print(our_get(dict_1, 2))
# print(our_get(dict_1, 1))
# print(our_get(dict_1, 3, default_value="Пусто"))
# print(our_get(dict_1, [1, 3]))


# 📌Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class LevelError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class AccessError(LevelError):
    def __init__(self):
        super().__init__('Ошибка данных доступа')


class PermError(LevelError):
    def __init__(self):
        super().__init__('Ошибка прав доступа')


# raise AccessError
# raise PermError

# 📌Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# 📌Передавайте необходимые данные из основного кода проекта.


# 📌Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор и
# уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# 📌Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# 📌Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
import os
import json

MIN_LVL = 1
MAX_LVL = 7


def create_json(path: str = 'users_sem13.json'):
    user_data = {}
    id_list = []
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as file:
                user_data = json.load(file)
        else:
            print("Нет файла")
            break
        if user_data:
            for users in user_data.values():
                for user in users:
                    id_list.append(user[1])
        name = input("Введите имя пользователя: ")
        if not name:
            break
    while True:
        u_id = input("Введите личный ID: ")
        if u_id.isdigit():
            if int(u_id) not in id_list:
                u_id = int(u_id)
                break
            else:
                print(f'ID {u_id} уже занят. Введите другой ID.')
        else:
            print('ID должен быть целым числом')
    while True:
        u_lvl = input("Введите уровень доступа: ")
        if u_lvl.isdigit() and MIN_LVL <= int(u_lvl) <= MAX_LVL:
            break
        else:
            print(f'Уровень доступа должен быть от {MIN_LVL} до {MAX_LVL}')

    if u_lvl in user_data:
        user_data[u_lvl].append((name, u_id))
    else:
        user_data[u_lvl] = [(name, u_id)]

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_data, file, indent=6, ensure_ascii=False)


create_json()


class User:
    def __init__(self, name: str, u_id: str, lvl: int):
        self.name = name
        self.u_id = u_id
        self.lvl = lvl



def load_users():
    users_set = set()
    with open('users_sem13.json', 'r', encoding='UTF-8') as file:
        data_users = json.load(file)
    for lvl, users in data_users.items():
        for user in users:
            name, u_id = user
            users_set.add(User(name, u_id, lvl))
    return users_set



data = load_users()
print(data)
