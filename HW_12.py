# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых
import csv


def gen_csv_with_disciplines():
    disciplines = [['math'], ['literature'], ['physics']]
    with open('csv_with_disciplines.csv', 'w', encoding='UTF-8', newline='') as f:
        f_writer = csv.writer(f, delimiter=',', dialect='excel')
        f_writer.writerows(disciplines)


gen_csv_with_disciplines()


class DisckriptorFIO:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not (value.istitle() and value.isalpha()):
            raise ValueError('Начинаться должно с большой, и иметь только буквы!')
        setattr(instance, self.name, value)


class DiscDiscipline:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        try:
            value.isdigit()
            2 <= int(value) <= 5
            setattr(instance, self.name, value)
        except:
            raise ValueError('от 2 до 5')


class Student:
    name = DisckriptorFIO()
    patronymic = DisckriptorFIO()
    sur_name = DisckriptorFIO()

    def __init__(self, name, patronymic, sur_name, **kwargs):
        self.name = name
        self.patronymic = patronymic
        self.sur_name = sur_name
        self._disciplines = {}
        with open('csv_with_disciplines.csv', 'r') as f:
            read = csv.reader(f)
            for el in read:
                self._disciplines[str(*el)] = 0
        for i, v in kwargs.items():

            if i in self._disciplines:
                self._disciplines[i]=v
            else:
                raise IOError (f'Нет такого предмета {i}!')

    def average_score(self):
        if {self._disciplines.values()} is not None:
            aver = sum(self._disciplines.values()) / len(self._disciplines.values())
            return round(aver, 2)
        else:
            return 'Неизвестно каким.'

    def __str__(self):
        return f'Студент {self.sur_name} {self.name} {self.patronymic} имеет следующие успехи в учёбе:\n' \
               f'{(self._disciplines)}\nИ средним баллом {self.average_score()}'


stud1 = Student("Вася", "Васильевич", "Васильев", math=5, literature=3)

print(stud1)