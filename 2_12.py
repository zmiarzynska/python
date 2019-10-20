line="Oto jest napis z ktorego potrzebujemy pierwsze i ostatnie litery"

tablica_wyrazow=line.split()
print(tablica_wyrazow)
napis_pierwszych=""
napis_ostatnich=""
for i in range(0,len(tablica_wyrazow)):
	slowo=tablica_wyrazow[i]
	napis_pierwszych+=slowo[0]

for i in range(0,len(tablica_wyrazow)):
	slowo2=tablica_wyrazow[i]
	index_litery=len(slowo2)-1
	napis_ostatnich+=slowo2[index_litery]

print(napis_pierwszych)
print(napis_ostatnich)
