#warunkiem jest podanie poprawnej liczby w systemie rzymskim
rzymska=input("Podaj liczbe w notacji rzymskiej: ")

slownik={
"0" :0,
"I" :1,
"V" :5,
"X" :10,
"L" :50,
"C" :100,
"D" :500,
"M" :1000
}
rzymska+="0"
arabska=0
liczba=0
for i in range(len(rzymska)-1):
	
	staraLiczba=liczba	
	liczba=slownik.get(rzymska[i])
	nast_liczba=slownik.get(rzymska[i+1])
	
	if (liczba>=nast_liczba):
		arabska+=liczba
	else:
		arabska-=liczba		
						
		

	
print("Liczba w systemie arabskim: ")
print(arabska)


