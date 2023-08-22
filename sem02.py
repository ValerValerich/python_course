# Создать лист, сет, лист с уникальными значениями без сета
import random


def task1():
    list_of_digit = [1, 1, 5, 76, 34, 5, 23, 5, 6565, 234]
    set_of_digit = set(list_of_digit)
    print(list_of_digit, set_of_digit, sep='\n')
    unic_list = []
    for i in list_of_digit:
        if i not in unic_list:
            unic_list.append(i)
    print(unic_list)


# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔Целое положительное число
# ✔Вещественное положительное или отрицательное число
# ✔Строку в верхнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔Строку в нижнем регистре в остальных случаях

def task2():
    input_user = input("Введите данные:\n")
    if input_user.isdigit():
        res = f"Вы ввели целое число {input_user}"
    elif (input_user.startswith('-') and input_user.replace('-', '', 1).replace('.', '', 1).isdigit()) or (
            input_user.replace('.', '', 1).isdigit()):
        res = f"Вы ввели вещественное число {float(input_user)}"
    elif len([i for i in input_user if i.isupper()]) > 0:
        res = f"Вы строке есть большая буква {input_user.upper()}"
    else:
        res = f"В тексте нет заглавных букв {input_user}"

    print(res)


# ✔Создайте вручную кортеж содержащий элементы разных типов.
# ✔Получите из него словарь списков, где:
# ключ — тип элемента, значение — список элементов данного типа.

def task3():
    tup = (2, [3, 5], 'f', 1.5, {23: '23'}, 'asdxas', 45)
    res_dict = {}
    for i in tup:
        if type(i) in res_dict:
            res_dict[type(i)].append(i)
        else:
            res_dict[type(i)] = [i]
    print(res_dict)


# ✔Создайте вручную список с повторяющимися элементами.
# ✔Удалите из него все элементы, которые встречаются дважды.
def task4():
    lst = [1, 2, 3, 1, 4, 3, 3, 5, 6, 7]
    for i in lst:
        if lst.count(i) == 2:
            lst.remove(i)
            lst.remove(i)
    print(lst)


# ✔Создайте вручную список с повторяющимися целыми числами.
# ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔Нумерация начинается с единицы

def task5():
    lst = [random.randint(0, 100) for _ in range(20)]
    print(lst)
    res = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            res.append(i + 1)
    print(res)


# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

def task6():
    text = sorted(input("Введите несколько слов\n").split())
    print(*text)
    length = len(max(text, key=len))
    for i, j in enumerate(text, 1):
        print(f"{i} {j.rjust(length, ' ')}")


# ✔Пользователь вводит строку текста.
# ✔Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

def task7():
    text = list(input("Введите текст\n"))
    temp_list = list(set(text))
    dict_with_count = {}
    dict_without_count = {}
    for i in temp_list:
        dict_with_count[i] = text.count(i)
    for j in text:
        if j in dict_without_count.keys():
            dict_without_count[j] += 1
        else:
            dict_without_count[j] = 1
    print(dict_with_count, dict_without_count, sep='\n')


# ✔Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔Какие вещи взяли все три друга
# ✔Какие вещи уникальны, есть только у одного друга
# ✔Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

def task8():
    turists = {"Vasiliy": (),
               "Vladimir": (),
               "Alex": ()}


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
task8()
