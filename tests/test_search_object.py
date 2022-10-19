from unittest import TestCase
from searchin.search_object import search_object


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
        for result in search_object(MyClass(), 'gamma'):
            print(result)
            self.assertEqual(result.query, 'gamma')
