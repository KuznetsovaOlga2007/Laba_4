import circle
import math
import unittest


class CircleTestCase(unittest.TestCase):
	def test_float(self):
		radius = 1 / math.pi
		self.assertAlmostEqual(circle.area(radius), 1 / math.pi)
		self.assertAlmostEqual(circle.perimeter(radius), 2.0)

	def test_radius_of_one(self):
		radius = 1
		self.assertAlmostEqual(circle.area(radius), math.pi)
		self.assertAlmostEqual(circle.perimeter(radius), 2 * math.pi)

	def test_some_radius(self):
		radius = 15
		self.assertAlmostEqual(circle.area(radius), math.pi * 225)
		self.assertAlmostEqual(circle.perimeter(radius), math.pi * 30)

	def test_big_radius(self):
		radius = 10_000
		self.assertAlmostEqual(circle.area(radius), math.pi * 100_000_000, places=4)
		self.assertAlmostEqual(circle.perimeter(radius), math.pi * 20_000)
