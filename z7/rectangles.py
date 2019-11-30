from points import Point




class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if x1>=x2 or y1>=y2:
            raise ValueError("To nie jest prostokat")

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1, self.pt2)
    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({0}, {1}, {2}, {3})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1==other.pt1 and self.pt2==other.pt2:
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self.__eq__(other)


    def center(self):          # zwraca środek prostokąta
        nowy_punkt = (self.pt2 - self.pt1)
        nowy_punkt.x /= 2
        nowy_punkt.y /= 2
        return nowy_punkt

    def area(self):            # pole powierzchni
        x = self.pt2.x - self.pt1.x
        y = self.pt2.y - self.pt1.y
        return x * y

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
        return self.pt1, self.pt2

    def intersection(self, other): # część wspólna prostokątów
        if (self.pt2.x<other.pt1.x or other.pt2.x<self.pt1.x) or (self.pt2.y<other.pt1.y or other.pt2.y<self.pt1.y) : #rozlaczne
            return 0
        else:
            x1=max(self.pt1.x,other.pt1.x)
            y1=max(self.pt1.y,other.pt1.y)
            x2=min(self.pt2.x,other.pt2.x)
            y2=min(self.pt2.y,other.pt2.y)
            return Rectangle(x1,y1,x2,y2)


    def cover(self, other):    # prostąkąt nakrywający oba
        x1=min(self.pt1.x,other.pt1.x)
        y1=min(self.pt1.y,other.pt1.y)
        x2=max(self.pt2.x,other.pt2.x)
        y2=max(self.pt2.y,other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca listę czterech mniejszych
        dlugosc=self.pt2.x-self.pt1.x
        wysokosc=self.pt2.y-self.pt1.y
        dlugosc/=2
        wysokosc/=2
        pierwszy=Rectangle(self.pt1.x,self.pt1.y,self.pt1.x+dlugosc,self.pt1.y+wysokosc)
        drugi=Rectangle(self.pt1.x+dlugosc,self.pt1.y,self.pt2.x,self.pt1.y+wysokosc)
        trzeci=Rectangle(self.pt1.x,self.pt1.y+wysokosc,self.pt1.x+dlugosc,self.pt2.y)
        czwarty=Rectangle(self.pt1.x+dlugosc,self.pt1.y+wysokosc,self.pt2.x,self.pt2.y)
        return pierwszy,drugi,trzeci,czwarty

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Rectangle(1,5,2,7)),"[(1, 5), (2, 7)]")
        self.assertEqual(repr(Rectangle(1,5,2,7)),"Rectangle(1, 5, 2, 7)")
        #self.assertEqual(str(Rectangle(2, 5, 1, 7)), "[(2, 5), (1, 7)]")

    def test_eq(self):
        self.assertEqual((Rectangle(1, 0, 2, 5) != Rectangle(1, 0, 2, 5)), False)
        self.assertEqual((Rectangle(1, 0, 2, 5) == Rectangle(1, 0, 2, 5)), True)

    def test_center(self):
        self.assertEqual(Rectangle.center(Rectangle(0,0,1,1)),Point(0.5,0.5))

    def test_area(self):
        self.assertEqual(Rectangle.area(Rectangle(0, 0, 1, 1)), 1)
        self.assertEqual(Rectangle.area(Rectangle(1, 2, 3, 4)), 4)


    def test_move(self):
        self.assertEqual(Rectangle.move(Rectangle(1,2,3,4),0,1),(Point(1,3),Point(3,5)))

    def test_intersection(self):
        self.assertEqual(Rectangle.intersection(Rectangle(1,1,2,2),Rectangle(0,0,2,2)),Rectangle(1,1,2,2))

    def test_cover(self):
        self.assertEqual(Rectangle.cover(Rectangle(0,0,2,2),Rectangle(1,1,2,2)),Rectangle(0,0,2,2))

    def test_make4(self):
        self.assertEqual(Rectangle.make4(Rectangle(0,0,2,2)),(Rectangle(0,0,1,1),Rectangle(1,0,2,1),Rectangle(0,1,1,2),Rectangle(1,1,2,2)))



if __name__ == "__main__":
    unittest.main()  # wszystkie testy
