class Queue:

    def __init__(self,size):
        self.items = []
        self.size=size
        self.amount=0
        if self.size<0:
            raise ValueError("size musi byc wieksze od 0")

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return self.size==self.amount


    def put(self, data):
        if self.is_full():
            raise IndexError("Kolejka jest pelna")
        else:
            self.items.append(data)
            self.amount+=1

    def get(self):
        if self.is_empty():
            raise IndexError("Kolejka jest pusta")
        else:
            self.amount-=1
            return self.items.pop(0)   # mało wydajne!


def przepelnienieKolejki():
    kolejka=Queue(1)
    kolejka.put(1)
    kolejka.put(1)

def pustaKolejka():
    kolejka2=Queue(2)
    kolejka2.get()


k=Queue(2)
k.put(1)
if k.is_empty():
    print("Kolejka pusta")
else:
    print("Kolejka nie jest pusta")

if k.is_full():
    print("Kolejka jest pelna")
else:
    print("Kolejka nie jest pelna")

#przepelnienieKolejki()                    # po odkomentowaniu program rzuci wyjatek

#pustaKolejka()                             # po odkomentowaniu program rzuci wyjatek