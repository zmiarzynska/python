def kopiuj(kopiowany,kopia):
	wejscie=open(kopiowany,"r")
	wyjscie=open(kopia,"w")
	for line in wejscie:
		print(line.index("#"))
		if line.index("#") is 0:
			print("komentarz")

		else:
			wyjscie.write(line)
		
	
	wejscie.close()
	wyjscie.close()

kopiuj("plik_tekstowy.txt","kopia.txt")
print("Wykonalo sie")
