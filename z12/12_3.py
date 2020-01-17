import copy

def sort_babel(L):               # Uzylam sortowania babelkowego
    temp=len(L)
    for i in range(len(L)):
        for j in range(temp-1):
            if L[j]>L[j+1]:
                L[j],L[j + 1]=L[j+1],L[j]
        temp-=1


def mediana_sort(L, left, right):
    if left<right:
        newL= copy.copy(L)
        sort_babel(newL)
        mid=(left+right)//2
        if (right - left)%2==0:
            return newL[mid]
        else:
            return (newL[mid]+newL[mid+1])/2
    return -1



L=[3,2,5,3,8,2,913,5,14,8]
print(L)
print(mediana_sort(L,0,9))


L=[3,2,5,3,8,2,913,4,14,8]
print(L)
print(mediana_sort(L,0,9))



