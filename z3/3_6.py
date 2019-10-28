x=int(input("Podaj dlugosc prostokata: "))

y=int(input("Podaj szerokosc prostokata: "))
prostokat=""
i=0
dlugosc=x+1
while dlugosc>0:
	if i%2==0:
		for j in range(y):
			prostokat+="+---"
			if j==(y-1):
				prostokat+="+"
				prostokat+="\n"
				i+=1
				dlugosc-=1
	
	else:
		for j in range(y):
			prostokat+="|   "
			if j==(y-1):
				prostokat+="|"
				prostokat+="\n"	
				i+=1
			
print(prostokat)
