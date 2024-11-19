import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area(self):
        x, y, z = 5, 12 ,13
        res = area(x,y,z)
        self.assertEqual(res,450)

    def test_perimeter(self):
        x,y,z = 5, 12 ,13
        res = perimeter(x,y,z)
        self.assertEqual(res,125)

    def test_area_negative(self):
        x,y,z = -5, -12, -13
        res = area(x,y,z)
        self.assertEqual(AssertionError,res)

    def test_perimeter_negative(self):
        x,y,z = -5, -12, -13
        res = perimeter(x,y,z)
        self.assertEqual(AssertionError,res)

    def test_area_zero(self):
        x,y,z = 0, 0, 0
        res = area(x,y,z)
        self.assertEqual(res,0)

    def test_perimeter_zero(self):
        x,y,z = 0, 0, 0
        res = perimeter(x,y,z)
        self.assertEqual(res,0)


if __name__ == '__main__':
    unittest.main()
