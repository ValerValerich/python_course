# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def pars_sting(text):
    *way, extantion = text.split(".")
    *way, file_name = str(*way).split('\\')
    return '\\'.join(way), file_name, extantion


# print(*pars_sting(input("Введите абсолютный адрес файла\n")))

# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
names = ['Ivan', 'Petr', 'Vlad']
price = [100, 150, 200]
award = ['10.25%', '35%', '50%']


def gen_prem(names, price, procent):
    yield {name: pri * float(proc[:-1]) / 100 for name, pri, proc in zip(names, price, procent)}


# print(gen_prem(names, price, award))

# Создайте функцию генератор чисел Фибоначчи

# Пришлось гуглить, не могло до меня дойти, что yield не обязан стоять в самом конце. начиналось с 1
def gen_fibo(n: int):
    first = 0
    second = 1
    for _ in range(n):
        yield first
        first, second = second, first + second

# print(*list(gen_fibo(10)))

