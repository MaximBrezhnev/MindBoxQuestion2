import unittest

from shapes import Circle, Triangle


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.get_area(), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0, places=5)

    def test_triangle_is_rectangular(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_rectangular())

        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_rectangular())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
