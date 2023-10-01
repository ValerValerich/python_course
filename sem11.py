# 📌Создайте класс Моя Строка, где:
# 📌будут доступны все возможности str
# 📌дополнительно хранятся имя автора строки и время создания (time.time)
import time
from functools import total_ordering

class MyString(str):
    """Это класс переопределяет метод str"""

    def __new__(cls, st, author):
        instance = super().__new__(cls, st)
        instance.author = author
        instance.st = st
        instance.time_ = time.time()
        return instance


strng = MyString("some text", 'Valeriy')


# print(strng, strng.author, strng.time_)


# 📌Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
# 📌list-архивы также являются свойствами экземпляра

class Archive:
    """Это класс является архивом созданных экземпляров"""

    _instance = None

    def __new__(cls, num, st):
        """Этот метод создает объект"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums = []
            cls._instance.sts = []
        else:
            cls._instance.nums.append(cls._instance.num)
            cls._instance.sts.append(cls._instance.st)
        return cls._instance

    def __init__(self, num, st):
        """Этот метод инициализирует поля объекта"""
        self.num = num
        self.st = st

    def __str__(self):
        """Этот метод переопределяет вывод информации по объекту в консоль"""
        return f"{self.num},{self.nums}, {self.st}, {self.sts}"

    def __repr__(self):
        return f'Archive({self.num}, "{self.st}")'


a = Archive(10, 'ten')
# print(a)
b = Archive(20, 'twenty')
# print(b)
c = Archive(30, 'thirsty')
# print(c)
# help(MyString)
# help(Archive)

# 📌Доработаем класс Архив из задачи 2.
# 📌Добавьте методы представления экземпляра для программиста и для пользователя.
a = Archive(4, 'fegawgf')


# print(f'{a=}')


# 📌Дорабатываем класс прямоугольник из прошлого семинара.
# 📌Добавьте возможность сложения и вычитания.
# 📌При этом должен создаваться новый экземпляр прямоугольника.
# 📌Складываем и вычитаем периметры, а не длинну и ширину.
# 📌При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if b is None else b

    def length(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            res = Rectangle.length(self) - Rectangle.length(other)
            if res < 0:
                return "Получается отрицательное число!"
            else:
                return Rectangle(self.a - other.a, self.b - other.b)
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Rectangle):
            res = Rectangle.length(self) + Rectangle.length(other)
            if res < 0:
                return "Получается отрицательное число!"
            else:
                return Rectangle(self.a + other.a, self.b + other.b)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError


rec1 = Rectangle(5)
rec2 = Rectangle(3, 4)
rec3 = rec1 - rec2
# print(rec3, rec3.length())
rec4 = rec3 + rec1
# print(rec4, rec4.length())

print(rec1 == rec4)
print(rec1 < rec4)
