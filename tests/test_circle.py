import unittest
from circle import area,perimeter
class test_circle(unittest.TestCase):
    def test_area(self):
        radius=5
        expected_area=78.5398163397
        actual_area=area(radius)
        self.assertEqual(actual_area,expected_area)
    
    def test_perimeter(self):
        radius=5
        expected_perimeter=31,41592653589793
        actual_perimeter=perimeter(radius)
        self.assertEqual(actual_perimeter,expected_perimeter)

if __name__=='__main__':
    unittest.main()