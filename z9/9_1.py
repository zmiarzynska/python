class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):  # klasy O(N)
        if self.length==0:
            raise ValueError('Lista jest pusta')
        self.length-=1
        node=self.head
        if self.head==self.tail:
            self.head=self.tail=None
        else:             #skracanie listy
            temp=self.head
            node=self.tail
            while temp.next!=None:
                if(temp.next==self.tail):
                    node=self.tail
                    temp.next=None
                    self.tail=temp
                    return node
                temp=temp.next
        return node


    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):  # klasy O(1)\
        if other.length == 0:
            pass
        if self.length == 0:
            self.head=other.head
            self.tail=other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        self.length += other.count()
        other.clear()



    # Węzły z listy other są przepinane do listy self na jej koniec.

    def clear(self): # czyszczenie listy
        self.length=0
        self.head=None
        self.tail=None



wezel=Node(5)
wezel2=Node(4,wezel)
wezel3=Node(3,wezel2)
wezel4=Node(2,wezel3)

lista=SingleList()

lista.insert_head(wezel)
lista.insert_tail(wezel2)
lista.insert_tail(wezel3)
lista.insert_tail(wezel4)

#print(lista.count())
print(lista.remove_tail())
print(lista.count())   #3 wezly

lista2=SingleList()
lista2.insert_head(wezel4)
lista2.insert_tail(wezel3)
lista2.insert_tail(wezel2)
lista2.insert_tail(wezel) # 4 wezly
#print(lista2.count())
lista.merge(lista2)
print(lista.count())
print(lista.remove_tail())

lista.clear()
print(lista.is_empty())
