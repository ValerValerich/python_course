# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата
from fractions import Fraction


def out_10_in_16():
    res_16 = ""
    num = int(input("Введите десятеричное число для перевода в шестнадцатеричное\n"))
    num_alter = num
    dict_for_repl = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    while num > 0:
        temp = (num % 16)
        if temp >= 10:
            dict_out = dict_for_repl[temp]
        else:
            dict_out = temp
        res_16 = str(dict_out) + res_16
        num //= 16
    print("Кастом:", res_16, "Стандарт:", hex(num_alter).replace("0x", ""), sep="\n")


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

def working_with_fractions():
    first_fract = input("Будем работать с дробями\nВведите первую дробь в формате х/y:\n")
    second_fract = input("Введите вторую дробь в формате х/y:\n")

    first_list = list(map(int, first_fract.split('/')))
    second_list = list(map(int, second_fract.split('/')))

    plus_fract = str(
        int(((first_list[0] * second_list[1] + second_list[0] * first_list[1])) / (first_list[1] * second_list[1]))) \
                 + "_" + str(((((first_list[0] * second_list[1]) + (second_list[0] * first_list[1]))) % \
                              (first_list[1] * second_list[1]))) + "/" + str(first_list[1] * second_list[1])

    multy_fract = str(int((first_list[0] * second_list[0]) / (first_list[1] * second_list[1]))) + "_" + str(
        int((first_list[0] * second_list[0]) % (first_list[1] * second_list[1]))) + "/" + str(
        first_list[1] * second_list[1])

    print("Собственный метод:", plus_fract, multy_fract, sep="\n")
    print("С использованием Fraction():", Fraction(first_fract) + Fraction(second_fract),
          Fraction(first_fract) * Fraction(second_fract), sep="\n")


# out_10_in_16()
# working_with_fractions()
