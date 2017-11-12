import unittest
from exponent import power


class TestMyExponent(unittest.TestCase):
    def test_the_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_negative_exponent(self):
        self.assertEqual(power(-2, 3), -8)


if __name__ == '__main__':
    unittest.main()
