# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# умножения матриц

class Matrix:
    """Данный метод позволяет выводить матрицу на печать, сравнивать,
    складывать и перемножать матрицы друг на друга и на число,
    проверяя поданные на вход атрибуты"""

    # Проверка входящих данных для матрицы на ~квадратность~
    @staticmethod
    def check_lst(in_data: list):
        if isinstance(in_data, list):
            if in_data and all(len(row) == len(in_data) for row in in_data):
                return in_data
            else:
                raise IOError("Нужна квадратная матрица")
        else:
            raise TypeError("На вход подана не квадратная матрица!")

    # проверка other на подходящую размерность
    @staticmethod
    def check_other(self_, other_):
        return all(len(row1) == len(other_row) for row1, other_row in zip(self_, other_))

    def __init__(self, lst):
        self.lst = Matrix.check_lst(lst)

    def __str__(self):
        res = [row for row in self.lst]  # не вышло в ретерне передать матрицу построчно с переносом строк(
        return f'Объект класса Матрица {res}'

    def __eq__(self, other: list):
        if isinstance(other, Matrix) and Matrix.check_other(self.lst, other.lst):
            return all(r1 == r2 for r1, r2 in zip(self.lst, other.lst))
        else:
            raise TypeError("Попытка сравнения матриц разной размерности!")

    def __add__(self, other):
        if isinstance(other, Matrix) and Matrix.check_other(self.lst, other.lst):
            res = []
            for row1, row2 in zip(self.lst, other.lst):
                res.append([el1 + el2 for el1, el2 in zip(row1, row2)])
            return Matrix(res)

    def __mul__(self, other: (list, int, float)):
        try:  # если умножить предлагается на число
            float(other)
            res = []
            for row in self.lst:
                res.append([el * other for el in row])
            return Matrix(res)
        except:  # иначе работаем с перемножением матриц
            if isinstance(other, Matrix) and Matrix.check_other(self.lst, other.lst):
                res = []
                for row1, row2 in zip(self.lst, other.lst):
                    res.append([el1 * el2 for el1, el2 in zip(row1, row2)])
                return Matrix(res)
            else:
                raise TypeError('Попытка перемножения матриц разной размерности!')


m1 = Matrix([[1, 2, 4], [-7, 1, 2], [0, 1, 0]])
m2 = Matrix([[1, 2, 4], [-7, 1, 2], [0, 1, 0]])
# m2 = Matrix([[1, 'b', 4], [0, 1, 2], [0, 1, 0]])
# m2 = Matrix([[1, 'b', 4], [0, 1, 2], [0, 1, 0], [0, 1, 0]])
# m2 = [[0, 1], [0, 2]]

print(f'Матрица m1 {m1}')
print(f'Матрица m2 {m2}')

print(f'Сравнение матрицы m1 и m2. Равны? {m1 == m2}')
print(f'Результат перемножение двух матриц: {m1 * m2}')
print(f'Результат перемножение матрицы на число: {m1 * 3}')
print(f'Результат сложения матриц: {m1 + m1}')
print(m1)
