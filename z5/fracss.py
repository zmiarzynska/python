from math import gcd
import unittest

def NWW(a,b):
    return a/gcd(a,b)*b

def add_frac(frac1, frac2):      # frac1 + frac2
    wielokrotnosc=NWW(frac1[1],frac2[1])
    print(wielokrotnosc)
    temporary=[frac1[0]*wielokrotnosc/frac1[1],frac1[1]*wielokrotnosc/frac1[1],frac2[0]*wielokrotnosc/frac2[1],frac2[1]*wielokrotnosc/frac2[1]]
    print(temporary)
    nowy=[]
    nowy.append(int(temporary[0]+temporary[2]))
    nowy.append(int(frac1[1]*wielokrotnosc/frac1[1]))
    print(nowy)
    dzielnik=gcd(nowy[0],nowy[1])
    nowy[0]/=dzielnik
    nowy[1]/=dzielnik
    print(nowy)
    return nowy


def sub_frac(frac1, frac2):       # frac1 - frac2
    wielokrotnosc = NWW(frac1[1], frac2[1])
    print(wielokrotnosc)
    temporary = [frac1[0] * wielokrotnosc / frac1[1], frac1[1] * wielokrotnosc / frac1[1],
                 frac2[0] * wielokrotnosc / frac2[1], frac2[1] * wielokrotnosc / frac2[1]]
    print(temporary)
    nowy = []
    nowy.append(int(temporary[0] - temporary[2]))
    nowy.append(int(frac1[1] * wielokrotnosc / frac1[1]))
    print(nowy)
    dzielnik = gcd(nowy[0], nowy[1])
    nowy[0] /= dzielnik
    nowy[1] /= dzielnik
    print(nowy)
    return nowy

def mul_frac(frac1, frac2):        # frac1 * frac2
    mnozenie=[frac1[0]*frac2[0],frac1[1]*frac2[1]]
    dzielnik = gcd(mnozenie[0], mnozenie[1])
    mnozenie[0] /= dzielnik
    mnozenie[1] /= dzielnik
    return mnozenie
def div_frac(frac1, frac2):         # frac1 / frac2
    mnozenie=[frac1[0] * frac2[1], frac1[1] * frac2[0]]      
    dzielnik = gcd(mnozenie[0], mnozenie[1])
    mnozenie[0] /= dzielnik
    mnozenie[1] /= dzielnik
    return mnozenie

def is_positive(frac):             # bool, czy dodatni
    if (frac[0]>=0 and frac[1]>=0 ) or (frac[0]<0 and frac[1]<0 ):
        return True
    else:
        return False

def is_zero(frac):                 # bool, typu [0, x]
    if frac[0]==0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):      # -1 | 0 | +1
    if (frac1[0]==frac2[0] and frac1[1]==frac2[1]):
        return 0
    elif (is_positive(sub_frac(frac1, frac2))):
        return 1
    else:
        return -1


def frac2float(frac):              # konwersja do float
    liczbaFloat=frac[0]/frac[1]
    return liczbaFloat

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, -2]                   # zero (niejednoznaczność)


#print(div_frac(f1,f2))
#print(frac2float(f1))
print(add_frac(f1,f4))
print(sub_frac(f1,f4))
print(cmp_frac(f1,f4))


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1,2],[1,3]),[1,6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2,3],[4,5]),[8,15])

    def test_div_frac(self):
        self.assertEqual(div_frac([2,3],[4,5]),[5,6])

    def test_is_positive(self):
        self.assertFalse(is_positive([-2,1]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0,7]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([2,3],[1,3]),1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1,4]),0.25)

    def tearDown(self):
        self.zero = [0, 1]

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
