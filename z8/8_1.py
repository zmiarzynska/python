
def solve1(a,b,c):
    if(a!=0 and b!=0):
        wspolczynnik1=-a/b
        wspolczynnik2=-c/b
        return "Rozwiazanie ma postac prostej'y={0}*x + ({1})'".format(wspolczynnik1, wspolczynnik2)
    elif (a==0  and b!=0):
        wspolczynnik2 = -c / b
        return "Rozwiazanie ma postac 'y={0}'".format(wspolczynnik2)
    elif (a!=0 and b==0):
        wspolczynnik1 = -c/a
        return "Rozwiazanie ma postac 'x={0}'".format(wspolczynnik1)

    else:
        if (a==0 and b==0):
            if c==0:
                return "Rownanie tozsamosciowe"
            else:
                return "Rownanie sprzeczne"



print(solve1(0, 0, 0))

print(solve1(0, 0, 5))

print(solve1(3, 0, 8))

print(solve1(1, 2, 6))

