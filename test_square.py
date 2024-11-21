import square
import unittest


class SquareTestCase(unittest.TestCase):
	def test_float(self):
		a = 0.3
		self.assertAlmostEqual(square.area(a), 0.09)
		self.assertAlmostEqual(square.perimeter(a), 1.2)

	def test_some_side(self):
		a = 12
		self.assertEqual(square.area(a), 144)
		self.assertEqual(square.perimeter(a), 48)

	def test_side_of_one(self):
		a = 1
		self.assertEqual(square.area(a), 1)
		self.assertEqual(square.perimeter(a), 4)

	def test_big_side(self):
		a = 100_000
		self.assertEqual(square.area(a), 10_000_000_000)
		self.assertEqual(square.perimeter(a), 400_000)
