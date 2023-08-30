# Пользователь вводит строку из четырех или более целых чисел, разделенных символом /
# Сформировать словарь, где:
# Второе и третье число является ключами;
# Первое число является значением для первого ключа;
# Четвертое и все возможные поледующие числа хранятся в кортеже как значение второго ключа

def one_str():
    in_str = list(map(int, input("Введите целые числа через '/'\n").split('/')))
    a, b, c, *d = in_str
    some_dict = {b: a, c: tuple(d)}
    print(some_dict)


# one_str()

# Самостоятельно сохранить в переменную строку текста.
# Создать из строки словарь, где ключ - буква, а значение - код буквы
#  Написать преобразование в одну строку

def dict_from_string():
    print({i: ord(i) for i in input('Введите текст\n')})


# dict_from_string()

# Пробежаться итератором 5 раз по словарю из прошлой задачи

def inerator():
    old_dict = {i: ord(i) for i in input('Введите текст\n')}
    dict_iter = iter(old_dict.items())
    for _ in range(5):
        print(*next(dict_iter))


# inerator()

# Написать генератор четных чисел, не дающих сумму составляющих цифр 8 от 0 до 100

# print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))

# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, выводит "Fizz".
# Вместо чисел, кратных пяти  - слово "Buzz".
# Если число кратно и 3 и 5 - "FizzBuzz".
# Реализовать в формате генератора

def gen_fizz_buzz():
    return ("FizzBuzz" if i % 3 == i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in
           range(1, 101))
# print(*gen_fizz_buzz(), sep='\n')

# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с 2.

def gen_primery_num(n):
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i %j == 0:
                is_prime =False
                break
        if is_prime:
            yield i

for num, optimus in enumerate(gen_primery_num(100), start=1):
    print(f'{num} = {optimus}')