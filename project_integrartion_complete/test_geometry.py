import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestGeometry(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(-1, 4), -4)
    
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(-1, 4), 6)
    
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(-1), 3.141592653589793)
    
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(3), 18.84955592153876)
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(-1), -6.283185307179586)

if __name__ == '__main__':
    unittest.main()
