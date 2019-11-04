def rysuj_miarke(miarka):
    print(miarka)
    miarka += 1
    gorna = ""
    dolna = ""
    for i in range(0, miarka):
        for j in range(5):
            if j % 5 == 0:
                gorna += "|"
                dolna += str(i)
                if i < 9:
                    dolna += '    '
                else:
                    dolna += '   '
            else:
                if i == (miarka - 1):
                    pass
                else:
                    gorna += "."

    # print(gorna)
    # print(dolna)
    linijka = gorna + "\n" + dolna
    return linijka


def rysuj_prostokat(x, y):
    prostokat = ""
    i = 0
    dlugosc = x + 1
    while dlugosc > 0:
        if i % 2 == 0:
            for j in range(y):
                prostokat += "+---"
                if j == (y - 1):
                    prostokat += "+"
                    prostokat += "\n"
                    i += 1
                    dlugosc -= 1

        else:
            for j in range(y):
                prostokat += "|   "
                if j == (y - 1):
                    prostokat += "|"
                    prostokat += "\n"
                    i += 1
    return prostokat








dlugosc = int(input("Podaj dlugosc miarki: "))
obiekt: str = rysuj_miarke(dlugosc)
print(obiekt)

dlugosc = int(input("Podaj dlugosc prostokata: "))
szerokosc = int(input("Podaj szerokosc prostokata: "))

print(rysuj_prostokat(dlugosc, szerokosc))