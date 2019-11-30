from points import Point
import math
class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):      # "Circle(x, y, radius)"
        return 'Circle({0}, {1}, {2})'.format(self.pt.x,self.pt.y,self.radius)
    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):         # pole powierzchni
        return self.radius**2*math.pi
    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y
        return repr(self)

    def cover(self, other):    # okrąg pokrywający oba
        dlugosc=math.sqrt((self.pt.x-other.pt.x)**2+(self.pt.y-other.pt.y)**2)
        mini= min(self.radius,other.radius)
        maxi= max(self.radius,other.radius)
        if (dlugosc<maxi and dlugosc > mini) or dlugosc==0:
            if self.radius>other.radius:
                return Circle(self.pt.x,self.pt.y,self.radius)
            else:
                return Circle(other.pt.x,other.pt.y,other.radius)
        else:
            dlugosc+=self.radius
            dlugosc+=other.radius
            dlugosc/=2   #promien
            x=(self.pt.x+other.pt.x)/2
            y=(self.pt.y+other.pt.y)/2
            return Circle(x, y, dlugosc)

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    def test_print(self):
        self.assertEqual(repr(Circle(1,5,5)),"Circle(1, 5, 5)")

    def test_area(self):
        self.assertEqual(Circle.area(Circle(1,5,5)),(25*math.pi))

    def test_move(self):
        self.assertEqual(Circle.move(Circle(1,5,5), 0, 1),"Circle(1, 6, 5)")
        #self.assertEqual(Circle.move(Circle(1, 5, -1), 0, 1), "Circle(1, 6, 5)")

    def test_cover(self):
        self.assertEqual(Circle.cover(Circle(1, 1, 1),Circle(3, 1, 1)), Circle(2, 1, 2))
        self.assertEqual(Circle.cover(Circle(0, 0, 5), Circle(1, 1, 1)), Circle(0, 0, 5))
        self.assertEqual(Circle.cover(Circle(1, 2, 1), Circle(1, 2, 2)), Circle(1, 2, 2))


if __name__ == "__main__":
    unittest.main()  # wszystkie testy