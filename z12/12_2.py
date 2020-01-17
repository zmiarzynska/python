def binarne_rek(L, left, right, y):
    if(left>right):
        return -1
    mid=(left+right)//2
    if(y==L[mid]):
        return mid
    if(y<L[mid]):
        return binarne_rek(L,left,mid-1,y)
    else:
        return binarne_rek(L,mid+1,right,y)



L=[3,5,7,8,12,16,18,34]

print(binarne_rek(L,0,7,15))
print(binarne_rek(L,0,7,25))
print(binarne_rek(L,0,7,35))
print(binarne_rek(L,0,7,-1))

print(binarne_rek(L,0,7,3))

print(binarne_rek(L,0,7,5))

print(binarne_rek(L,0,7,7))

print(binarne_rek(L,0,7,8))

print(binarne_rek(L,0,7,12))

print(binarne_rek(L,0,7,16))

print(binarne_rek(L,0,7,18))

print(binarne_rek(L,0,7,34))
