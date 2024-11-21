import triangle
import unittest


class TriangleTestCase(unittest.TestCase):
	def test_float_area(self):
		a = 0.5
		h = 0.9
		self.assertAlmostEqual(triangle.area(a, h), 0.225)

	def test_float_perimeter(self):
		a = 0.3
		b = 0.5
		c = 0.2
		self.assertAlmostEqual(triangle.perimeter(a, b, c), 1.0)

	def test_big_area(self):
		a = 1000
		h = 900
		self.assertAlmostEqual(triangle.area(a, h), 450_000)

	def test_big_perimeter(self):
		a = 8_000_000
		b = 1_234_567
		c = 10_000_000
		self.assertEqual(triangle.perimeter(a, b, c), 19_234_567)

	def test_some_area(self):
		a = 1
		h = 1
		self.assertAlmostEqual(triangle.area(a, h), 0.5)

	def test_some_perimeter(self):
		a = 1
		b = 1
		c = 1
		self.assertEqual(triangle.perimeter(a, b, c), 3)
