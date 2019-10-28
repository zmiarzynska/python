sekwencja=[[],[4],(1,2),[3,4],(5,6,7)]

suma_sekwencji=[]
suma=0

for i in range(len(sekwencja)):
	for j in range(len(sekwencja[i])):
		#print("i j %i %i, %i"%(i,j ,sekwencja[i][j]))
		suma+=sekwencja[i][j]
	suma_sekwencji.append(suma)
	suma=0

print(suma_sekwencji)
