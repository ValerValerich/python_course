# 📌Создайте класс окружность.
# 📌Класс должен принимать радиус окружности при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие длину окружности и её площадь.
import random
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return round(2 * pi * self.radius, 5)

    def area(self):
        return round(pi * self.radius ** 2, 5)


krug = Circle(5)


# print(krug.area())
# print(krug.length())

# 📌Создайте класс прямоугольник.
# 📌Класс должен принимать длину и ширину при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие периметр и площадь.
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if b is None else b

    def length(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


rec1 = Rectangle(5, 6)


# print(rec1.length())
# print(rec1.area())

# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Human:
    def __init__(self, last_name, name, age, patronymic=None):
        self._name = name
        self._last_name = last_name
        self._patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def full_name(self):
        return f'{self._last_name} {self._name} {"" if self._patronymic is None else self._patronymic} c {self._age} лет'


# stone = Human('Панфилов', 'Кирилл', 39, 'Владимирович')
# alisa = Human('Худякова', 'Алиса', 18)
#
# print(stone.full_name())
# print(alisa.full_name())
#
# stone.birthday()
# print(stone.full_name())

class Employee(Human):
    def __init__(self, last_name, name, age, patronymic):
        super().__init__(last_name, name, age, patronymic)
        self.u_id = str(random.randint(1, 999999)).zfill(0)
        self.lvl_access = int(self.u_id) % 7


stone = Employee('Панфилов', 'Кирилл', 39, 'Владимирович')


# print(stone.u_id)
# print(stone.lvl_access)

# 📌Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Animal:
    def __init__(self, name, age, special):
        self.name = name
        self.age = age
        self.special = special

    def get_special(self):
        return self.special


class Dog(Animal):
    def __init__(self, name, age, **kwargs):
        super().__init__(name, age, kwargs.get('breed', None))


class Cat:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.special = kwargs.get('color', None)

    def get_special(self):
        return self.special


class Fish:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.special = kwargs.get('habitat', None)

    def get_special(self):
        return self.special


spanky = Dog('Cпанки', 3, breed="yuork")
tom = Cat('Tom', 15, color="Blue")
dorry = Fish('Dorry', 1, habitat="Дом")

for animal in [spanky, tom, dorry]:
    print(animal.get_special())
