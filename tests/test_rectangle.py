import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):

    def test_area(self):
        # Тесты для функции вычисляющей площадь
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(3, 7), 21)
        self.assertEqual(area(2.5, 4), 10.0)

    def test_perimeter(self):
        # Тесты для функции вычисляющей периметр
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(3, 7), 20)
        self.assertEqual(perimeter(2.5, 4), 13.0)

if __name__ == '__main__':
    unittest.main()
