class Stack:

    def __init__(self,maxsize):
        self.items = []
        self.size=maxsize
        self.amount=0
        if self.size<0:
            raise ValueError("size musi byc wieksze od 0")

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        if self.size==self.amount:
            return True
        else:
            return False


    def push(self, item):
        if self.is_full():
            raise IndexError("Stos jest pelny")
        else:
            self.items.append(item)         # dodajemy na koniec
            self.amount+=1


    def pop(self):                      # zwraca element
        if self.is_empty():
            raise IndexError("Stos jest pusty")
        else:
            self.amount-=1
            return self.items.pop()         # zabieram od końca




def przepelnienieStosu():
    stos1 = Stack(3)
    stos1.push(1)
    stos1.push(2)
    stos1.push(3)
    print(stos1)
    stos1 = Stack(2)
    stos1.push(1)
    stos1.push(2)
    stos1.push(3)      #rzuca wyjatek
    print(stos1.pop()) #nie wykona się


def pustyStos():
    stos2=Stack(5)
    stos2.pop() #rzuca wyjatek



s=Stack(2)
if s.is_empty():
    print("Stos pusty")
else:
    print("Stos nie jest pusty")

if s.is_full():
    print("Stos jest pelny")
else:
    print("Stos nie jest pelny")

#pustyStos()  # po odkomentowaniu program rzuci wyjatek

#przepelnienieStosu() # po odkomentowaniu program rzuci wyjatek





