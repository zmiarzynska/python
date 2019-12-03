import time
P={}



def dynamic(i,j):
    if (i==0 and j==0):
        return 0.5
    if (i>0 and j==0):
        return 0
    if (i==0 and j>0):
        return 1
    if(i>0 and j>0):
        if(i,j) in P:
            return P[(i,j)]
        else:
            wynik=0.5*(dynamic(i-1,j)+dynamic(i,j-1))
            P[(i,j)]=wynik
            return wynik



def recursive(i,j):
    if (i==0 and j==0):
        return 0.5
    if (i>0 and j==0):
        return 0
    if (i==0 and j>0):
        return 1
    if (i>0 and j>0):
        return 0.5*(recursive(i-1,j)+recursive(i,j-1))
    else:
        return -1

czas_rekurencyjny = time.time()
print(recursive(10,5))
print("recursive(10,5) czas:", time.time()-czas_rekurencyjny)
czas_dynamiczny = time.time()
print(dynamic(10,5))
print("dynamic(10,5) czas:", time.time()-czas_dynamiczny)


#Rekurencja jest bardziej zasobożerna i zajmuje więcej czasu

