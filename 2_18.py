duza_liczba=1094345830482305068936590860858304860380

liczba_napis=str(duza_liczba)
cyfry_zero=0
print(len(liczba_napis))
for i in range(0,len(liczba_napis)):
	if int(liczba_napis[i])==0:
		cyfry_zero+=1


print("Cyfr 0 w powyzszej duzej liczbie: %i"%cyfry_zero)
