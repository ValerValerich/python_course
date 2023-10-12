# 📌Создайте функцию, которая удаляет из текста все символы кроме букв
# латинского алфавита и пробелов. 📌Возвращается строка в нижнем регистре.

from string import ascii_lowercase


def del_other_symbol(str_: str) -> str:
    """
    >>> del_other_symbol('wew wefefe') == 'wew wefefe'
    True
    >>> del_other_symbol('wew wefeFE') == 'wew wefefe'
    True
    >>> del_other_symbol('wew _wefefe,.:;') == 'wew wefefe'
    True
    >>> del_other_symbol('wew _wыавываefefe,.:;') == 'wew wefefe'
    True
    >>> del_other_symbol('Wew _wыавываefefe,.:;') == 'wew wefefe'
    True
    """
    str_ = str_.lower()
    res = ''
    for sym in str_:
        if sym in ascii_lowercase + ' ':
            res += sym

    return res


# print(del_other_symbol('xfgfrKJUiu KIU kjh43 hukh 23232 123 h huk'))


# 📌Напишите для задачи 1 тесты doctest.
# Проверьте следующие варианты:
# 📌возврат строки без изменений
# 📌возврат строки с преобразованием регистра без потери символов
# 📌возврат строки с удалением знаков пунктуации
# 📌возврат строки с удалением букв других алфавитов
# 📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

# То же, но при помощи unittest в файле sem14test.py
# то же, с pytest в фалйе sem14pytest.py
# Тест класса rectangle в файле sem14testRect.py
