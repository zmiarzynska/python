lista_1=["a",3,2,7,9,7,8,8,8]
lista_2=[1,"a",3,3,5,6,7,4,8]

print(lista_1)
print(lista_2)
w_obu=[]
wszystkie_b_powt=[]
liczba=4
wszystkie_b_powt.extend(lista_1)
wszystkie_b_powt.extend(lista_2)

i=0

while( i <= len(wszystkie_b_powt)-1):
	liczba=wszystkie_b_powt[i] 
	b=wszystkie_b_powt.count(liczba)
	if b>1:
		liczba=wszystkie_b_powt.pop(i)
		i-=1
	i+=1

 
i=0

while( i <= len(lista_1)-1):
	
	liczba=lista_1[i]
	b=lista_1.count(liczba)
	i+=1
	if b>1:
		liczba=lista_1.pop(i)
		i-=1
		pass
	if b==1:
		czy_jest=lista_2.count(liczba)
		if czy_jest>0:
			w_obu.append(liczba)
print("Wszystkie bez powtorzen")
print(wszystkie_b_powt)
print("W obu: ")
print(w_obu)
