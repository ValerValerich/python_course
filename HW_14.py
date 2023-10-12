# 📌На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌Напишите 3-7 тестов unittest для данного проекта.
# 📌Используйте setUp

from HW_12 import Student
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.f_user = Student("Iv", "Ivanich", "Ivanov")


    def test_name(self):

        self.assertTrue(len(self.f_user.name()) > 3, msg='Слишком короткое имя')


if __name__ == '__main__':
    unittest.main()
