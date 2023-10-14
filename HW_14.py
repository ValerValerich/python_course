# 📌На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌Напишите 3-7 тестов unittest для данного проекта.
# 📌Используйте setUp

from HW_12 import Student  # с юзерами из 13 семинара у меня беда, взял студентов
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.f_user = Student("Ivan", "Ivanich", "Ivanov")


    def test_len_name(self):
        self.assertGreaterEqual(len(self.f_user.name), 3)


    def test_name_title(self):
        with self.assertRaises(ValueError):
            self.s_user = Student("timur", "Ivanich", "Ivanov")

    def test_patronymic(self):
        self.assertTrue(self.f_user.patronymic.isalpha())



if __name__ == '__main__':
    unittest.main(verbosity=True)
