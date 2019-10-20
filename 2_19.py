L=[2,300,444,55]

print(L)
#nowa_lista=[]
napis=" "
for i in range(0,len(L)):
	liczba=str(L[i])
	#nowa_lista.append(liczba.zfill(3))
	napis+=liczba.zfill(3)
	napis+=" "

#print(nowa_lista)
print(napis)


