import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator("add", 2, 3), 5)

	def test_subtract(self):
		self.assertEqual(calculator("subtract", 7, 4), 3)

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator("multiply", 2, 3)


if __name__ == "__main__":
	unittest.main()
