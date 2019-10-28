import math


while True:
	line=input("Podaj liczbe typu float: ")
	
	if line=="stop":	
		break
	else:
			
		try:
			number = float(line)
			thirdpower=math.pow(number,3)
			print(number,thirdpower)
		except ValueError:
			print("Value Error")
