from unittest import TestCase
from searchin import searchin


class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def my_method(self):
        gamma = 1

    def my_other_method(self):
        pass


class Test(TestCase):
    def test_search_object(self):
        for result in searchin(MyClass(), 'gamma'):
            print(result)
            self.assertEqual(result.query, 'gamma')
