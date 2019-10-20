line="napisy w linii ktory jest najdluzszy i jaka ma dlugosc"

tablica_wyrazow=line.split()
max_licznik=0
max_slowo=0
for i in range(0,len(tablica_wyrazow)):
	licznik_liter=0
	for j in range(0,len(tablica_wyrazow[i])):
		licznik_liter+=1
	if max_licznik < licznik_liter:
		max_licznik=licznik_liter
		max_slowo=i+1

print("Najdluzsze slowo ma %i"%max_licznik,end="")
print(" liter")
print("Jest to slowo nr %i"%max_slowo)

