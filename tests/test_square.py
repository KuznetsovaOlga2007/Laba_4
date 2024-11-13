import unittest
from square import area, perimeter

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # Тесты для функции вычисляющей площадь
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3), 9)

    def test_perimeter(self):
        # Тесты для функции вычисляющей периметр
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)

if __name__ == '__main__':
    unittest.main()
