import unittest
from divide import divide_two
class TestMyDivision(unittest.TestCase):
	"""docstring forTestMyDivision"""
	def test_simple_division(self):
		self.assertEqual(divide_two(60,5),12)
		
	def test_one_negative_number(self):
		self.assertEqual(divide_two(-20,5),-4)

	def test_two_negative_number(self):
		self.assertEqual(divide_two(-30,-5),6)

if __name__ == '__main__':
	unittest.main()
