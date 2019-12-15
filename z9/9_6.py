class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def count_leafs(top):
        if top is None:
            return 0
        liscie=0
        stack = list()
        stack.append(top)
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if(node.left==None and node.right==None ):
                liscie+=1
        return liscie

    def count_total(top):
        if top is None:
            return 0
        suma=0
        stack = list()
        stack.append(top)
        while stack:
            node = stack.pop()
            suma+=node.data
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return suma





root = None           # puste drzewo
root = Node("start")  # drzewo z jednym węzłem
# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.count_leafs())
print(root.count_total())
