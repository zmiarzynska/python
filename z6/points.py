import copy
import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self.__eq__(other)

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        nowy_punkt=copy.copy(self)
        nowy_punkt.x+=other.x
        nowy_punkt.y+=other.y
        return nowy_punkt

    def __sub__(self, other):  # v1 - v2
        nowy_punkt = copy.copy(self)
        nowy_punkt.x -= other.x
        nowy_punkt.y -= other.y
        return nowy_punkt

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        multiply=(self.x*other.x)+(self.y*other.y)
        return multiply

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt((self.x)**2+(self.y)**2)


# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p = Point(0,0)

    def test_print(self):
        self.assertEqual(str(Point(1,5)),"(1, 5)")
        self.assertEqual(repr(Point(20,30)), "Point(20, 30)")
        self.assertEqual(Point(20, 30) != Point(20, 30), False)
        self.assertEqual(Point(20, 30) == Point(20, 30), True)

    def test_add(self):
        self.assertEqual(Point(1,2)+Point(2,4), Point(3,6))

    def test_sub(self):
        self.assertEqual(Point(4,7)-Point(5,2), Point(-1,5))

    def test_mul(self):
        self.assertEqual(Point(6,2)*Point(3,2), Point(18,4))

    def test_cross(self):
        self.assertEqual(Point.cross(Point(1,2),Point(2,3)), -1)

    def test_length(self):
        self.assertEqual(Point(3,4).length(),5)



if __name__ == "__main__":
    unittest.main()  # wszystkie testy
