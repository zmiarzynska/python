import random

class RandomQueue:

    def __init__(self,size):
        self.items = []
        self.size=size
        self.amount=0
        if self.size<0:
            raise ValueError("size musi byc wieksze od 0")

    def insert(self, item):
        if self.is_full():
            raise IndexError("Kolejka jest pelna")
        else:
            self.items.append(item)
            self.amount+=1

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise IndexError("Kolejka jest pusta")
        else:
            rand=random.randint(0, self.amount-1)
            i=(self.amount-1)-rand
            print(i)
            temp = self.items[i]
            self.items[i]=self.items[len(self.items)-1]
            self.items[len(self.items)-1]=None
            self.amount -= 1
            return temp



    def is_empty(self):
        return not self.items

    def is_full(self):
        return self.size==self.amount

    def clear(self):     # czyszczenie listy
        self.items=[]
        self.amount=0


randomKolejka=RandomQueue(10)
randomKolejka.insert(1)
randomKolejka.insert(2)
print(randomKolejka.remove())
