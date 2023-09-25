# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random


def gen_csv_with_random_int():
    qty_str_in_csv = random.randint(100, 1000)
    with open('csv_for_hw_09.csv', 'w', encoding='UTF-8') as f:
        csv_writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(('a', 'b', 'c'))
        for _ in range(qty_str_in_csv):
            csv_writer.writerow((random.randint(-1000, 1000), \
                                 random.randint(-1000, 1000), \
                                 random.randint(-1000, 1000)))


gen_csv_with_random_int()


def start_func_with_csv_parametr(func):
    def wrap_func():
        with open('csv_for_hw_09.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].isdigit():
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(result)

    return wrap_func


def save_in_json(*a):
    print(*a)
    def get_func(func):
        def wrap_in_json(*args):
            res = func(*args)
            data = {
                "args": args,

                "res": res
            }
            with open("json_with_parametrs_func.json", 'w') as json_f:
                json.dump(data, json_f)

        return wrap_in_json

    return get_func


@save_in_json
@start_func_with_csv_parametr
def root_search(a, b, c):
    if b ** 2 - 4 * a * c > 0:
        x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return round(x1, 5), round(x2, 5)
    elif b ** 2 - 4 * a * c == 0:
        return round(-b / (2 * a), 5)
    else:
        return "Нет корней"
