line="Trzeba posortowac linie w porzadku alfabetycznym oraz wedlug dlugosci slow w linii"
print(line)
line=line.lower()
line2=line.split()
print("Sortowanie alfabetyczne:")
print(sorted(line2))

print("Sortowanie wedlug dlugosci wyrazow:")
print(sorted(line2,key=len))
