import unittest
import math

'''
r (float): radius of circle
return value (float): area of circle
'''
def circle_area(r: float) -> float:
  if r < 0:
    raise ValueError("Invalid radius of circle")
  return round(math.pi * r * r, 10)

'''
r (float): radius of circle
return value (float): perimeter of circle
'''
def circle_perimeter(r: float) -> float:
  if r < 0:
    raise ValueError("Invalid radius of circle")
  return round(2 * math.pi * r, 10)


class TriangleTestCase(unittest.TestCase):
  def test_one_area(self):
    res = circle_area(1)
    self.assertEqual(res, 3.1415926536)

  def test_integer_area(self):
    res = circle_area(673)
    self.assertEqual(res, 1422918.4189977713)
  
  def test_float_area(self):  
    res = circle_area(983.023)
    self.assertEqual(res, 3035828.48184314)

  def test_negative_first_value_excaption_area(self):
    self.assertRaises(ValueError, circle_area, -456)

  def test_one_perimetr(self):
    res = circle_perimeter(1)
    self.assertEqual(res, 6.2831853072)

  def test_integer_perimeter(self):
    res = circle_perimeter(893)
    self.assertEqual(res, 5610.8844793114)
  
  def test_float_perimeter(self):
    res = circle_perimeter(7384.12345)
    self.assertEqual(res, 46395.8159674402)

  def test_negative_first_value_excaption_perimeter(self):
    self.assertRaises(ValueError, circle_perimeter, -98345)
