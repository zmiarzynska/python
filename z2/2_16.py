line="tekst znajdujacy sie w zmiennGvRej o nazwie line\t"

print(line)
czy_wystepuje=line.find('GvR')
line_2=""
if czy_wystepuje>0:
	for i in range(0,czy_wystepuje):
		line_2+=line[i]
	line_2+="Guido van Rossum"
	for i in range(czy_wystepuje+3,len(line)):
		line_2+=line[i]
line=line_2
print(line)
