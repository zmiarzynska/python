
miarka = int(input("Podaj dlugosc miarki: "))
print(miarka)
miarka+=1
gorna=""
dolna=""
for i in range(0,miarka):
	for j in range(5):
		if j%5==0:
			gorna+="|"
			dolna+=str(i)
			if i<9:	
				dolna+='    '
			else:
				dolna+='   '	
		else:
			if i==(miarka-1):
				pass
			else:			
				gorna+="."
	
#print(gorna)
#print(dolna)
linijka =gorna+"\n"+dolna
print(linijka)
