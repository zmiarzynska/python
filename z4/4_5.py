def odwracanie(L, left, right):
    while(left<right):
        temp=L[right]
        L[right]=L[left]
        L[left]=temp
        left+=1
        right-=1


def revlist(L,left,right):  #rekurencyjnie
    if left<right:
        tempor=L[right]
        L[right]=L[left]
        L[left]=tempor
        left+=1
        right-=1
        revlist(L,left,right)

lista=[1,2,3,4]
odwracanie(lista,1,3)
print(lista)
revlist(lista,1,3)
print(lista)