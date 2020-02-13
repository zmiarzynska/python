line="Jaka jest laczna dlugosc wyrazow w tym napisie "

tablica_wyrazow=line.split()
laczna_suma=0
for i in range(0,len(tablica_wyrazow)):
	for j in range(0,len(tablica_wyrazow[i])):
		laczna_suma+=1

print(laczna_suma)
