# 📌Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌Экземпляр должен запоминать последние k значений.
# 📌Параметр k передаётся при создании экземпляра.
# 📌Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
import json


class Factorial:
    def __init__(self, limit):
        self.limit = limit
        self.function = []

    @property
    def fact(self):
        fact = 1
        values = []
        for i in range(1, self.limit + 1):
            fact *= i
            values.append(fact)
        return values

    def __call__(self, number):
        self.function = self.fact[-number:]
        return self.function

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('factorial_res.json', 'w', encoding='UTF-8')
        json.dump(self.function, file)
        file.close()


# l = Factorial(10)
# print(l.fact)
# print(l(3))

# 📌Доработаем задачу 1. 📌Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

# with Factorial(10) as fac_10:
#     print(fac_10(4))
#
# print("Конец")


class Factor:
    def __init__(self, a=None, b=None, c=None):
        variables = {a, b, c}.difference({None})
        if len(variables) == 1:
            self.start, self.stop, self.step = 1, a, 1
        elif len(variables) == 2:
            self.start, self.stop, self.step = a, b, 1
        else:
            self.start, self.stop, self.step = a, b, c
        self.fact = self.factorial()

    def factorial(self):
        fact_list = []
        num = 1
        for i in range(self.start, self.stop + 1, self.step):
            num *= i
            fact_list.append(num)
        return fact_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.fact:
            return self.fact.pop(0)
        raise StopIteration


first = Factor(10)
second = Factor(4, 8)
third = Factor(5, 12, 3)


# for i in first:
#     print(i)
# print()
# for i in second:
#     print(i)
# print()
# for i in third:
#     print(i)


# 📌Доработайте класс прямоугольник из прошлых семинаров.
# 📌Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# 📌Используйте декораторы свойств.

class Reactangle:
    __slots__ = ('_side_a', '_side_b')

    def __init__(self, side_a: float, side_b: float = None):
        if side_a <= 0 or side_b <= 0:
            raise ValueError
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    @property
    def side_a(self):
        return self._side_a

    @property
    def side_b(self):
        return self._side_b

    @side_a.setter
    def side_a(self, value):
        if value <= 0:
            raise ValueError
        self._side_a = value

    @side_b.setter
    def side_b(self, value):
        if value <= 0:
            raise ValueError
        self._side_b = value

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a} и {self.side_b}'


# rec = Reactangle(4, 5)
# print(rec)
# rec.side_a = 20
# print(rec)
# # print(rec.__dict__) Ошибка, т.к. мы ограничили доступ к атрибутам через slots
# print(rec.__slots__)


# Дискриптор


class Length:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError
        setattr(instance, self.name, value)


class Reactangle_2:
    side_a = Length()
    side_b = Length()

    def __init__(self, side_a: float, side_b: float = None):
        # if (side_a or side_b) <= 0:
        #     raise ValueError
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a} и {self.side_b}'


rect = Reactangle_2(4, 5)
print(rect)
rect.side_b = 10
print(rect)
