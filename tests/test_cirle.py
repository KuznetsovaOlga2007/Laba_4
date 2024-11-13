import unittest
from circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        # Тесты для функции вычисляющей площадь
        self.assertAlmostEqual(area(0), 0)

        self.assertAlmostEqual(area(1), 3.141592653589793)

        self.assertAlmostEqual(area(2), 12.566370614359172)

        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_perimeter(self):
        # Тесты для функции вычисляющей периметр
        self.assertAlmostEqual(perimeter(0), 0)

        self.assertAlmostEqual(perimeter(1), 6.283185307179586)

        self.assertAlmostEqual(perimeter(2), 12.566370614359172)

        self.assertAlmostEqual(perimeter(3), 18.84955592153876)

if __name__ == '__main__':
    unittest.main()
