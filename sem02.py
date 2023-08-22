# Создать лист, сет, лист с уникальными значениями без сета

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
     pass

# task1()
# task2()
# task3()
