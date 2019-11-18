from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def same_point(self, point1, point2):
        """Porównaj punkty."""
        return (point1.x == point2.x) and (point1.y == point2.y)

    def greater_than(self, point2,point1):
        return (point1.x<point2.x or point1.y<point2.y)

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):       # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1,self.pt2)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x,self.pt1.y, self.pt2.x,self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return ((self.same_point(self.pt1,other.pt1) and self.same_point(self.pt2,other.pt2) ) or(self.same_point(self.pt1,other.pt2) and self.same_point(self.pt2,other.pt1) ) )

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self.__eq__(other)

    def center(self):          # zwraca środek prostokąta
        nowy_punkt=(self.pt2-self.pt1)
        nowy_punkt.x/=2
        nowy_punkt.y/=2
        return nowy_punkt

    def area(self):           # pole powierzchni
        x=self.pt2.x-self.pt1.x
        y=self.pt2.y-self.pt1.y
        return x*y

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x+=x
        self.pt2.x+=x
        self.pt1.y += y
        self.pt2.y += y
        return self.pt1,self.pt2

# Kod testujący moduł.
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.p = Rectangle(0,0,1,1)

    def test_print(self):
        self.assertEqual(str(Rectangle(1,0,2,3)),"[(1, 0), (2, 3)]")
        self.assertEqual(repr(Rectangle(1,0,2,3)),"Rectangle(1, 0, 2, 3)")
        self.assertEqual((Rectangle(1, 0, 2, 5) != Rectangle(1, 0, 2, 5)), False)
        self.assertEqual((Rectangle(1, 0, 2, 5) == Rectangle(1, 0, 2, 5)), True)

    def test_center(self):
        self.assertEqual(Rectangle.center(Rectangle(0,0,1,1)),Point(0.5,0.5))

    def test_area(self):
        self.assertEqual(Rectangle.area(Rectangle(0,0,1,1)),1)
        self.assertEqual(Rectangle.area(Rectangle(1, 2, 3, 4)), 4)

    def test_move(self):
        self.assertEqual(Rectangle.move(Rectangle(1,2,3,4),0,1),(Point(1,3),Point(3,5)))

if __name__ == "__main__":
    unittest.main()     # wszystkie testy