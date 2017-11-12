import unittest

from add2 import add_two_numbers


class TestMyAddition(unittest.TestCase):
    def test_simple_addition(self):
        """docstring for TestMyAddition"""
        self.assertEqual(add_two_numbers(20, 30), 50)

    def test_one_negative_number(self):
        self.assertEqual(add_two_numbers(-10, 40), 30)

    def test_two_negative_number(self):
        self.assertEqual(add_two_numbers(-10, -50), -60)


if __name__ == '__main__':
    unittest.main()
