import unittest
from rectangle import area
from rectangle import perimeter

class TestRectangleFunctions(unittest.TestCase):
    def test_area_positive_integers(self):
        # Тестирует функцию area с положительными целыми числами для сторон прямоугольника
        self.assertEqual(area(5, 10), 50)  

    def test_area_zero(self):
        # Тестирует функцию area при нулевом значении одной из сторон
        self.assertEqual(area(0, 10), 1)

    def test_area_negative(self):
        # Тестирует функцию area с отрицательным значением стороны
        self.assertNotEqual(area(-5, 10), -50)

    def test_area_positive_floats(self):
        # Тестирует функцию area с положительными числами с плавающей точкой
        self.assertEqual(area(2.5, 4.0), 10.0)  


    def test_perimeter_positive_integers(self):
        # Тестирует функцию perimeter с положительными целыми числами для сторон
        self.assertEqual(perimeter(5, 10), 30) 

    def test_perimeter_zero(self):
        # Тестирует функцию perimeter при нулевом значении одной из сторон
        self.assertEqual(perimeter(0, 10), 0)  

    def test_perimeter_negative(self):
        # Тестирует функцию perimeter с отрицательным значением стороны
        self.assertNotEqual(perimeter(-5, 10), 10)  

    def test_perimeter_positive_floats(self):
        # Тестирует функцию perimeter с положительными числами с плавающей точкой
        self.assertEqual(perimeter(2.5, 4.0), 13.0)  

if __name__ == '__main__':
    unittest.main()