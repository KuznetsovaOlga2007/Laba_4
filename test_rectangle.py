import rectangle
import unittest


class RectangleTestCase(unittest.TestCase):
	def test_float(self):
		a = 0.3
		b = 0.5
		self.assertAlmostEqual(rectangle.area(a, b), 0.15)
		self.assertAlmostEqual(rectangle.perimeter(a, b), 1.6)

	def test_big_sides(self):
		a = 100_000
		b = 2_000
		self.assertEqual(rectangle.area(a, b), 200_000_000)
		self.assertEqual(rectangle.perimeter(a, b), 204_000)

	def test_equal_sides(self):
		a = 34
		self.assertEqual(rectangle.area(a, a), 1156)
		self.assertEqual(rectangle.perimeter(a, a), 136)

	def test_some_sides(self):
		a = 14
		b = 23
		self.assertEqual(rectangle.area(a, b), 322)
		self.assertEqual(rectangle.perimeter(a, b), 74)
