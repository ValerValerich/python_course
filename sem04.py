# ✔Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы. ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки
import random


def task1():
    text = sorted(input("Введите несколько слов\n").split())
    print(*text)
    length = len(max(text, key=len))
    for i, j in enumerate(text, 1):
        print(f"{i} {j.rjust(length, ' ')}")


# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию
def task2():
    text = input("Введите ваш текст\n")
    text = sorted(map(ord, list(set(text))), reverse=True)
    print(*text)


# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно

# nums = input("Введите два числа через пробел\n")
def task3(in_data):
    in_data = list(map(int, in_data.split()))
    my_dict = {chr(i): i for i in range(min(in_data), max(in_data) + 1)}
    print(my_dict)


# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

lst = [6, 4, 2, 6, 6, 4, 5, 3, 2, 4, 4, 5, 5, 4, 3, 4]


def task4(lst_input):
    for i in range(len(lst_input)):
        for j in range(len(lst_input) - i - 1):
            if lst_input[j] > lst_input[j + 1]:
                lst_input[j], lst_input[j + 1] = lst_input[j + 1], lst_input[j]
    print(lst)


# ✔Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔Сумма рассчитывается как ставка умноженная на процент премии
names = ['Ivan', 'Petr', 'Vlad']
price = [100, 150, 200]
award = ['10.25%', '35%', '50%']


def task5(imena, stavka, procent):
    res_dict = {imena[i]: stavka[i] * float((procent[i])[:-1]) / 100 for i in range(len(imena))}
    return res_dict


# ✔Функция получает на вход список чисел и два индекса.
# ✔Вернуть сумму чисел между переданными индексами.
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

# length_list = int(input("Введите длину списка\n"))
# list_for_task6 = [random.randint(0, 100) for _ in range(length_list)]
# first_ind, second_ind = map(int, input("Введите первый и второй индекс через пробел\n").split())
# print(list_for_task6)

def task6(lst: list, first_int, second_int):
    # ind1 = 0
    # ind2 = len(lst)
    # if ind1 < min(first_int, second_int) < ind2:
    #     ind1 = min(first_int, second_int)
    # if ind1 < max(first_int, second_int) < ind2:
    #     ind2 = max(first_int, second_int)
    print(lst[min(first_int, second_int):max(first_int, second_int) + 1])
    return sum(lst[min(first_int, second_int):max(first_int, second_int) + 1])


# ✔Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь

# dict_company = {'Рога и копыта': [500, 100, -300],
#                 'Супер-фирма': [-10000, 5000, 4000, 100],
#                 'Мутные типы': [800000, 50000, 1, 5, 12, 4, 5, 2]}


def task7(some_dict):
    res_lst = [(False, True)[sum(i) >= 0] for i in some_dict.values()]
    return all(res_lst)


# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None.
# ✔Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

nameses = 'STONE'
ages = [54, 76]
line = 8
s = 'S'
word = 'WORD'


def task8():
    global print_var

    def rename_sa():
        temp_dict = {}
        temp_dict.update(globals())
        for key, item in temp_dict.items():
            if not key.startswith('__') and key.endswith('s') and len(key) > 1:
                globals()[key] = None
                globals()[key[:-1]] = item

    def print_var(some_dict):
        for key, item in some_dict.items():
            if not key.startswith('__') and not type(item) == type(print_var):
                print(f'{key} = {some_dict[key]}')

    print_var(globals())
    rename_sa()
    print_var(globals())




# task1()
# task2()
# task3(nums)
# task4(lst)
# print(task5(names, price, award))
# print(task6(list_for_task6, first_ind, second_ind))
# print(task7(dict_company))
# task8()